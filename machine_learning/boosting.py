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
import pulp

class Adaboost():
    def __init__(self,
                 base_estimator=DecisionTreeClassifier(),
                 n_estimators=50,
                 learning_rate=1.):
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate

    def fit(self, x, y):
        n = len(y)
        d = np.zeros([self.n_estimators + 1, n])
        d[0] = np.array([1.0/n] * n)

        w = np.array([0.0] * self.n_estimators)
        classifiers = []

        for t in range(self.n_estimators):
            clf = self.base_estimator
            clf.fit(x, y, sample_weight=d[t])
            y_predict = clf.predict(x)
            u = (y_predict == y).astype(int)
            u[u==0] = -1
            accuracy = np.dot(d[t], u)
            w[t] = np.log((1+accuracy)/(1-accuracy))/2
            d[t+1] = d[t] * np.exp(-w[t] * u)
            d[t+1] = d[t+1]/d[t+1].sum() # normalize to sum 1
            classifiers.append(clf)

        self.classifiers = classifiers
        self.classifier_weights = w/w.sum()
        return self

    def predict(self, x):
        y_predict = np.array([0.0]*len(x))
        for index, clf in enumerate(self.classifiers):
            y_predict += clf.predict(x) * self.classifier_weights[index]
        y_predict[y_predict>=0.5] = 1
        y_predict[y_predict<0.5] = 0
        return y_predict


class LPboost():
    def __init__(self,
                 base_estimator=DecisionTreeClassifier(),
                 n_estimators=50,
                 learning_rate=1.):
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate

    def fit(self, x, y):
        n = len(y)
        d = np.zeros([self.n_estimators + 1, n])
        d[0] = np.array([1.0/n] * n)

        w = np.array([0.0] * self.n_estimators)
        # edges = np.

        classifiers = []

        for t in range(self.n_estimators):
            clf = self.base_estimator
            clf.fit(x, y, sample_weight=d[t])
            y_predict = clf.predict(x)
            u = (y_predict == y).astype(int)
            u[u==0] = -1
            accuracy = np.dot(d[t], u)
            w[t] = np.log((1+accuracy)/(1-accuracy))/2
            d[t+1] = d[t] * np.exp(-w[t] * u)
            d[t+1] = d[t+1]/d[t+1].sum() # normalize to sum 1
            classifiers.append(clf)

        self.classifiers = classifiers
        self.classifier_weights = w/w.sum()
        return self