import numpy as np

def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()#TODO

    ### fit the classifier on the training features and labels
    #TODO
    X = np.array(features_train)
    Y = np.array(labels_train)
    clf.fit(X, Y)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)#TODO
    assert len(pred) == len(labels_test)


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    ### accuracy = no. of points classified correctly / all points (in test set)
    total = 0
    for i in range(len(pred)):
        if pred[i] == labels_test[i]:
            total += 1
    accuracy = float(total) / (len(labels_test)) #TODO
    return accuracy