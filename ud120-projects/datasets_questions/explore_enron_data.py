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

import sys
sys.path.insert(0, '..\\final_project')

def get_num_of_pois():
    fin = open('..\\final_project\\poi_names.txt', 'r')
    num_of_names = 0
    for l in fin.readlines():
        if '(y)' in l or '(n)' in l:
            num_of_names += 1
    fin.close()
    return num_of_names


pprint(enron_data['LAY KENNETH L'])
pprint(enron_data['SKILLING JEFFREY K'])
pprint(enron_data['FASTOW ANDREW S'])