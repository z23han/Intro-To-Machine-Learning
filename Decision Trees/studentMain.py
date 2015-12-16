#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--it's your job to fill this in!
clf = classify(features_train, labels_train)



#################################################################################

########################## DECISION TREE #################################


#### your code goes here

from sklearn.metrics import accuracy_score

pred = clf.predict(features_test)
### you fill this in!
acc = accuracy_score(pred, labels_test)
### be sure to compute the accuracy on the test set



def submitAccuracies():
  return {"acc":round(acc,3)}



#### grader code, do not modify below this line
'''
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
'''