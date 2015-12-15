from sklearn.naive_bayes import GaussianNB
import numpy as np

def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier

    ### your code goes here!
    X = np.array(features_train)
    Y = np.array(labels_train)
    clf = GaussianNB()
    clf.fit(X, Y)
    return clf
