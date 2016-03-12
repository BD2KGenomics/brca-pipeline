import pandas as pd
from sklearn import preprocessing, cross_validation
from sklearn import tree, metrics, neighbors, linear_model, svm, ensemble
from IPython.display import Image, display
from sklearn.externals.six import StringIO
import pydot
from matplotlib import pyplot as plt


import plot_example
import helper

ALL_ALGOS = {"Decision tree": tree.DecisionTreeClassifier(max_depth=7, min_samples_leaf=10),
             "Random Forest": ensemble.RandomForestClassifier(),
             "KNN": neighbors.KNeighborsClassifier(),
             "Logistic regression": linear_model.LogisticRegression(),
             "SVM": svm.SVC(kernel="rbf"),
             "Ada Boost": ensemble.AdaBoostClassifier(),
             "Perceptron": linear_model.Perceptron(n_iter=100)}


def main():
    df = pd.read_csv("data/BRCA_data_with_label_final")
    df_encoded = encode_label(df)
    data, label = data_label_split(df_encoded)

    x_train, x_test, y_train, y_test = cross_validation.train_test_split(
        data, label, test_size=0.1, random_state=0)

    result = Random_forest_variation(x_train, y_train)
    print result.mean()
    plot_example.bar_plot(result)

def Random_forest_variation(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = helper.folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()

        for max_depth in range(2, 20):
            clf = ensemble.RandomForestClassifier(max_depth=max_depth)
            clf.fit(tr_data, tr_targets)
            prediction = clf.predict(val_data)
            accuracy = metrics.accuracy_score(prediction, val_targets)
            result_df.loc[foldnum, "max_depth={0}".format(max_depth)] = accuracy

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

def majority_vote(tr_data, tr_targets, val_data, val_targets):
    good_classifiers = ["Decision tree", "Random Forest", "KNN", "SVM", "Ada Boost"]
    estimators = [(i, ALL_ALGOS[i]) for i in good_classifiers]
    voting = ensemble.VotingClassifier(estimators=estimators)
    voting.fit(tr_data, tr_targets)
    prediction = voting.predict(val_data)
    accuracy = metrics.accuracy_score(prediction, val_targets)
    return accuracy


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