""" implementing Adaboost and LPBoost based on
Manfred Warmuth's video lecture and boosting tutorial which can be found here:
Video: http://videolectures.net/icml09_warmuth_vishwanathan_sbop/
Slide: https://users.soe.ucsc.edu/~manfred/pubs/tut/purdue2011.pdf

Variables in this script is named based on the slide, such as
d: weight vector of the samples
w: weight vector of hypothesis/learner
u: accuracy of prediction at each iteration
"""
from sklearn.tree import DecisionTreeClassifier
import numpy as np




class Adaboost():
    def __init__(self,
                 base_estimator=DecisionTreeClassifier,
                 n_estimators=2,
                 initial_learning_rate=1.):
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.initial_learning_rate = initial_learning_rate

    def fit(self, x, y):
        n = len(y)
        d = np.zeros([self.n_estimators + 1, n])
        d[0] = np.array([1.0/n] * n)
        print d

        w = np.array([0] * self.n_estimators)
        w[0] = self.initial_learning_rate
        for t in range(self.n_estimators):
            clf = self.base_estimator()
            clf.fit(x, y)
            y_predict = clf.predict(x)
            u = (y_predict == y.as_matrix()).astype(int)
            u[u==0] = -1
            w[t] = np.log((1 + np.dot(d[t], u))/(1 - np.dot(d[t], u)))/2
            d[t+1] = d[t] * np.exp(-w[t] * u)




            if (u==1).sum() == 0:
                pass
                # do something about perfect classification








class LPboost():
    pass