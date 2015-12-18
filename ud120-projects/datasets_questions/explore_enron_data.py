#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
from pprint import pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

def get_num_of_features():
    num_of_features = 0
    for key in enron_data.keys():
        if enron_data[key]['poi']:
            num_of_features += 1
    return num_of_features

