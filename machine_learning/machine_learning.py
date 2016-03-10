import pandas as pd
from sklearn import preprocessing, cross_validation
from sklearn import tree, metrics, neighbors, linear_model, svm, ensemble
from IPython.display import Image, display
from sklearn.externals.six import StringIO
import pydot
from matplotlib import pyplot as plt

classifiers = {"Decision tree": tree.DecisionTreeClassifier(),
               "Random Forest": ensemble.RandomForestClassifier(),
               "KNN": neighbors.KNeighborsClassifier(),
               "Logistic regression": linear_model.LogisticRegression(),
               "SVM": svm.SVC(kernel="rbf"),
               "Ada Boost": ensemble.AdaBoostClassifier(),
               "Perceptron": linear_model.Perceptron(n_iter=100)
               }


def folds_to_split(data,targets,train,test):
    data_tr = pd.DataFrame(data).iloc[train]
    data_te = pd.DataFrame(data).iloc[test]
    labels_tr = pd.DataFrame(targets).iloc[train]
    labels_te = pd.DataFrame(targets).iloc[test]
    return [data_tr, data_te, labels_tr, labels_te]


def main():
    df = pd.read_csv("raw_data/BRCA_data_with_label_final")
    df_encoded = encode_label(df)
    data, label = data_label_split(df_encoded)

    x_train, x_test, y_train, y_test = cross_validation.train_test_split(
        data, label, test_size=0.1, random_state=0)

    result = tenfold_cross_validation(x_train, y_train)
    print result.mean()
    plt.figure()
    result.mean().plot(kind="bar", sort_columns=True)
    plt.ylim([0.88, 0.98])
    plt.ylabel("accuracy score")
    plt.xticks(rotation=45)
    plt.show()


def feature_selection(x_train, y_train):
    """drop one feature each time to see which one has the
    greatest influence in the accuracy score"""
    for column in x_train.columns:
        x_train_drop = x_train.drop(column, axis=1)
        result = tenfold_cross_validation(x_train_drop, y_train)
        print "\ndrop out:" + column
        print result.mean()
        print "mean:", result.mean().mean()


def tenfold_cross_validation(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum = 0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum += 1
        [tr_data, val_data, tr_targets, val_targets] = folds_to_split(x_train, y_train, train, val)
        tr_targets = tr_targets.as_matrix().ravel()
        val_targets = val_targets.as_matrix().ravel()
        for classfier_name, clf in classifiers.iteritems():
            clf.fit(tr_data, tr_targets)
            prediction = clf.predict(val_data)
            accuracy = metrics.accuracy_score(prediction, val_targets)
            result_df.loc[foldnum, classfier_name] = accuracy
        result_df.loc[foldnum, "Voting"] = majority_vote(
            tr_data, tr_targets, val_data, val_targets)
    return result_df

def majority_vote(tr_data, tr_targets, val_data, val_targets):
    good_classifiers = ["Decision tree", "Random Forest", "KNN", "SVM", "Ada Boost"]
    estimators = [(i, classifiers[i]) for i in good_classifiers]
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