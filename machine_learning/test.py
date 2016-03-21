from sklearn import tree
from sklearn import cross_validation
from sklearn import metrics
import pandas as pd
import numpy as np

import boosting
import machine_learning

df = pd.read_csv("data/BRCA_data_with_label_final")
df_encoded = machine_learning.encode_label(df)
data, label = machine_learning.data_label_split(df_encoded)
x, x_test, y, y_test = cross_validation.train_test_split(data, label, test_size=0.1)

y = y.as_matrix()
clf = boosting.LPboost(n_estimators=2)
clf.fit(x, y)
#print metrics.accuracy_score(clf.predict(x_test), y_test)