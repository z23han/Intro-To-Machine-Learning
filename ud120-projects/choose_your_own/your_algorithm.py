#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
import sys

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

'''
1. k nearest neighbors
2. random forest
3. adaboost (also called boosted decision tree)
'''
from sklearn.metrics import accuracy_score
import numpy as np

X = np.array(features_train)
Y = np.array(labels_train)

opt = 2
if opt == 0:
    print 'run k-nearest-neighbors'
    from sklearn import neighbors
    clf = neighbors.KNeighborsClassifier(n_neighbors=1)
    clf.fit(X, Y)
    pred = clf.predict(features_test)
    ### you fill this in!
    acc = accuracy_score(pred, labels_test)
    print 'knn:', acc   # 0.94

elif opt == 1:
    print 'run random-forest'
    from sklearn import ensemble
    clf = ensemble.RandomForestClassifier()
    clf.fit(X, Y)
    pred = clf.predict(features_test)
    ### you fill this in!
    acc = accuracy_score(pred, labels_test)
    print 'random forest:', acc #0.916

elif opt == 2:
    print 'run adaboost'
    from sklearn import ensemble
    clf = ensemble.GradientBoostingClassifier()
    clf.fit(X, Y)
    pred = clf.predict(features_test)
    ### you fill this in!
    acc = accuracy_score(pred, labels_test)
    print 'adaboost:', acc  #0.912

else:
    print 'no such algorithm. Error input for opt'
    sys.exit()



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    print 'error in picturing!!'
    pass
