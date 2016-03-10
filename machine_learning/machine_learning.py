import pandas as pd
from sklearn import preprocessing, cross_validation, tree, metrics

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
    print result
    print result.mean()


def tenfold_cross_validation(x_train, y_train):
    result_df = pd.DataFrame()
    foldnum=0
    for train, val in cross_validation.KFold(len(x_train), shuffle=True, n_folds=10, random_state=0):
        foldnum+=1
        [tr_data, val_data, tr_targets, val_targets] = folds_to_split(x_train, y_train, train, val)
        clf = tree.DecisionTreeClassifier()
        clf.fit(tr_data, tr_targets)
        prediction = clf.predict(val_data)
        accuracy = metrics.accuracy_score(prediction, val_targets)
        result_df.loc[foldnum, 'decision tree'] = accuracy
    return result_df



def data_label_split(df):
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






                # (iris_te_data.values,
                #                                                                           iris_te_targets.values.ravel())
# print "Results for different parameters of K-Nearest Neighbors"
# print iris_knn_results.mean().apply(lambda x : '%0.3f' % x)









    # enc = preprocessing.OneHotEncoder()
    # enc.fit(df)
    # print enc.transform(df).toarray()








if __name__ == '__main__':
    main()