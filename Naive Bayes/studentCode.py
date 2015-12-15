from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from classify import NBAccuracy

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()
'''
print 'features_train:', features_train
print(len(features_train))
print 'labels_train:', labels_train
print(len(labels_train))
print 'features_test:', features_test
print(len(features_test))
print 'labels_test:', labels_test
print(len(labels_test))
'''

def submitAccuracy():
    accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test)
    return accuracy

print submitAccuracy()
