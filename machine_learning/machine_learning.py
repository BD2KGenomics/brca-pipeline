import pandas as pd
from sklearn import preprocessing, cross_validation
from sklearn import tree, metrics, neighbors, linear_model, svm, ensemble
from IPython.display import Image, display
from sklearn.externals.six import StringIO
import pydot
from matplotlib import pyplot as plt

import plotting
import helper
import boosting


ALL_ALGOS = {"Decision tree": tree.DecisionTreeClassifier(),
             "Random Forest": ensemble.RandomForestClassifier(),
             "KNN": neighbors.KNeighborsClassifier(),
             "Logistic regression": linear_model.LogisticRegression(),
             "SVM Linear": svm.SVC(kernel="linear"),
             "SVM RBF": svm.SVC(kernel="rbf"),
             "Ada Boost": ensemble.AdaBoostClassifier(),
             "Perceptron": linear_model.Perceptron(n_iter=100)}

FINAL_ALGOS = {"Decision tree": tree.DecisionTreeClassifier(max_depth=7, min_samples_leaf=10),
             "Random Forest": ensemble.RandomForestClassifier(max_depth=6, n_estimators=50),
             "KNN": neighbors.KNeighborsClassifier(n_neighbors=4, weights="distance"),
             "SVM RBF": svm.SVC(kernel="rbf", C=3, probability=True),
             "Ada Boost": ensemble.AdaBoostClassifier(n_estimators=50),}

BOOSTING = {"Adaboost_sklearn": ensemble.AdaBoostClassifier}
            # "Adaboost_Molly": boosting.Adaboost(),
            # "LPboost": boosting.LPboost()}



def main():
    df = pd.read_csv("data/BRCA_data_with_label_final")
    df_encoded = encode_label(df)

    data, label = data_label_split(df_encoded)
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(
        data, label, test_size=0.1, random_state=0)
    result = boosting_cv(x_train, y_train, BOOSTING)
    print result
    print result.mean()

def boosting_cv(x_train, y_train, classifiers):
    base_learners = {"DecisionTree": tree.DecisionTreeClassifier(),
                 "rbfSVM": svm.SVC(kernel="rbf", probability=True),
                 "linearSVM": svm.SVC(kernel="linear", probability=True)}

    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        for classfier_name, classifier in classifiers.iteritems():
            for base_learner_name, base_learner in base_learners.iteritems():
                clf = classifier(n_estimators=10, base_estimator=base_learner)
                clf.fit(tr_data, tr_targets)
                prediction = clf.predict(val_data)
                accuracy = metrics.accuracy_score(prediction, val_targets)
                result_df.loc[foldnum, "{0} {1}".format(classfier_name, base_learner_name)] = accuracy
    return result_df







def tenfold_cross_validation(x_train, y_train, classifiers):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        for classfier_name, clf in classifiers.iteritems():
            clf.fit(tr_data, tr_targets)
            prediction = clf.predict(val_data)
            accuracy = metrics.accuracy_score(prediction, val_targets)
            result_df.loc[foldnum, classfier_name] = accuracy
    return result_df


def perceptron_variation(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        for n in [1, 5, 10, 50, 100, 500, 1000]:
            clf = linear_model.Perceptron(n_iter=n)
            clf.fit(tr_data, tr_targets)
            prediction = clf.predict(val_data)
            accuracy = metrics.accuracy_score(prediction, val_targets)
            result_df.loc[foldnum, "n_iter={0}".format(n)] = accuracy
    return result_df


def real_test(x_train, y_train, x_test, y_test, FINAL_ALGO):
    results = {}
    voting_estimators = []
    for classfier_name, clf in FINAL_ALGOS.iteritems():
        voting_estimators.append((classfier_name, clf))
        clf.fit(x_train, y_train)
        prediction = clf.predict(x_test)
        accuracy = metrics.accuracy_score(prediction, y_test)
        results[classfier_name] = accuracy
    clf = ensemble.VotingClassifier(estimators=voting_estimators)
    clf.fit(x_train, y_train)
    accuracy = metrics.accuracy_score(clf.predict(x_test), y_test)
    results["Voting"] = accuracy
    return results


def lr_variation(x_train, y_train):
    result_df1 = pd.DataFrame()
    result_df2 = pd.DataFrame()
    weight_row_list = []

    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        # L1 regularization
        for C in [0.1, 1, 5, 10, 100, 10**3]:
            clf = linear_model.LogisticRegression(C=C, penalty="l1")
            clf.fit(tr_data, tr_targets)
            prediction = clf.predict(val_data)
            accuracy = metrics.accuracy_score(prediction, val_targets)
            result_df1.loc[foldnum, "C={0}".format(C)] = accuracy
            weight_dict = dict(zip(x_train.columns, clf.coef_[0]))
            weight_row_list.append(weight_dict)

        # L2 regularization
        for C in [0.1, 1, 5, 10, 100, 10**3]:
            clf = linear_model.LogisticRegression(C=C, penalty="l2")
            clf.fit(tr_data, tr_targets)
            prediction = clf.predict(val_data)
            accuracy = metrics.accuracy_score(prediction, val_targets)
            result_df2.loc[foldnum, "C={0}".format(C)] = accuracy
            weight_dict = dict(zip(x_train.columns, clf.coef_[0]))
            weight_row_list.append(weight_dict)

    weight_df = pd.DataFrame.from_dict(weight_row_list)

    return result_df1, result_df2, weight_df


def majority_vote(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        final_estimators = [(i, FINAL_ALGOS[i]) for i in FINAL_ALGOS.keys()]
        clf = ensemble.VotingClassifier(estimators=final_estimators)
        clf.fit(tr_data, tr_targets)
        prediction = clf.predict(val_data)
        accuracy = metrics.accuracy_score(prediction, val_targets)
        result_df.loc[foldnum, "Voting"] = accuracy
    return result_df


def ada_boost_variation(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        for n in [5, 10, 50, 100, 500, 1000]:
            clf = ensemble.AdaBoostClassifier(n_estimators=n)
            clf.fit(tr_data, tr_targets)
            prediction = clf.predict(val_data)
            accuracy = metrics.accuracy_score(prediction, val_targets)
            result_df.loc[foldnum, "n estimator={0}".format(n)] = accuracy
    return result_df


def svm_variation(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        for C in [0.1, 0.3, 0.5, 0.7, 1, 2, 3, 4, 5, 10, 100, 10**3, 10**5, 10**7, 10**9]:
            clf = svm.SVC(kernel="rbf", C=C)
            clf.fit(tr_data, tr_targets)
            prediction = clf.predict(val_data)
            accuracy = metrics.accuracy_score(prediction, val_targets)
            result_df.loc[foldnum, "C={0}".format(C)] = accuracy
    return result_df


def knn_variation(x_train, y_train):
    result_df_uniform = pd.DataFrame()
    result_df_distance = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        for n in range(1, 25):
            for w in ["uniform", "distance"]:
                clf = neighbors.KNeighborsClassifier(n_neighbors=n, weights=w)
                clf.fit(tr_data, tr_targets)
                prediction = clf.predict(val_data)
                accuracy = metrics.accuracy_score(prediction, val_targets)
                if w == "uniform":
                    result_df_uniform.loc[foldnum, "neigbhours={0}".format(n)] = accuracy
                elif w == "distance":
                    result_df_distance.loc[foldnum, "neigbhours={0}".format(n)] = accuracy

    return result_df_uniform, result_df_distance


def Random_forest_variation(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()
        clf = ensemble.RandomForestClassifier(max_depth=6,
                                              n_estimators=50)
        clf.fit(tr_data, tr_targets)
        prediction = clf.predict(val_data)
        accuracy = metrics.accuracy_score(prediction, val_targets)
        result_df.loc[foldnum, "best"] = accuracy
        clf = ensemble.RandomForestClassifier()
        clf.fit(tr_data, tr_targets)
        prediction = clf.predict(val_data)
        accuracy = metrics.accuracy_score(prediction, val_targets)
        result_df.loc[foldnum, "default"] = accuracy
    return result_df


def dtree_variations(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        clf_best = tree.DecisionTreeClassifier(
                                          max_depth=7,
                                          min_samples_leaf=10
                                          )
        clf_best.fit(tr_data, tr_targets)
        clf_default = tree.DecisionTreeClassifier()
        clf_default.fit(tr_data, tr_targets)

        prediction_default = clf_default.predict(val_data)
        prediction_best = clf_best.predict(val_data)
        accuracy_default = metrics.accuracy_score(prediction_default, val_targets)
        accuracy_best = metrics.accuracy_score(prediction_best, val_targets)
        result_df.loc[foldnum, "default setting"] = accuracy_default
        result_df.loc[foldnum, "best setting"] = accuracy_best

    return result_df


def feature_selection(x_train, y_train):
    """drop one feature each time to see which one has the
    greatest influence in the accuracy score"""
    for column in x_train.columns:
        x_train_drop = x_train.drop(column, axis=1)
        result = tenfold_cross_validation(x_train_drop, y_train)
        print "\ndrop out:" + column
        print result.mean()
        print "mean:", result.mean().mean()


def visualize_tree(dtree):
    dot_data = StringIO()
    tree.export_graphviz(dtree, out_file=dot_data,
                         filled=True, rounded=True,
                         special_characters=True)
    graph = pydot.graph_from_dot_data(dot_data.getvalue())
    display(Image(graph.create_png()))


def data_label_split(df):
    #df.drop("Comments", axis=1, inplace=True)
    label = df['Label']
    data = df.drop("Label", axis=1)
    return data, label

def encode_label(df):
    """
    transform non-numerical labels into numerical labels
    """
    df_encoded = pd.DataFrame()
    for column in df.columns:
        le = preprocessing.LabelEncoder()
        df_encoded[column] = le.fit_transform(df[column])
    return df_encoded


if __name__ == '__main__':
    main()