import pandas as pd
from sklearn import preprocessing, cross_validation, tree

def main():
    df = pd.read_csv("raw_data/BRCA_data_with_label_final")
    label = df['Label']
    data = df.drop("Label", axis=1)
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(
        data, label, test_size=0.1, random_state=0)

    result_df = pd.DataFrame()

    




    # clf = tree.DecisionTreeClassifier()
    # clf.fit(x_train, )




    # enc = preprocessing.OneHotEncoder()
    # enc.fit(df)
    # print enc.transform(df).toarray()








if __name__ == '__main__':
    main()