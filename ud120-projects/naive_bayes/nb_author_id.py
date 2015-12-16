#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("..\\tools")
from email_preprocess import preprocess
import numpy as np
from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


print 'features_train:', features_train
print len(features_train)
print 'features_test:', features_test
print len(features_test)
print 'labels_train:', labels_train
print len(labels_train)
print 'labels_test:', labels_test
print len(labels_test)


#########################################################
### your code goes here ###
X = np.array(features_train)
Y = np.array(labels_train)

clf = GaussianNB()

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)


assert len(pred) == len(labels_test)

total = 0
for i in range(len(pred)):
    if pred[i] == labels_test[i]:
        total += 1

accuracy = float(total) / len(labels_test)
print accuracy

#########################################################


