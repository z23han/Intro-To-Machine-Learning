#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
X = features_train
Y = labels_train

from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(X, Y)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score

acc = accuracy_score(pred, labels_test)

print acc
#########################################################


