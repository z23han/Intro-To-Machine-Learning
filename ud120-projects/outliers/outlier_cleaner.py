#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    diff = []
    for i in range(len(net_worths)):
        diff.append(abs(predictions[i] - net_worths[i]))
    indices = sorted(range(len(diff)), key=lambda k:diff[k])
    total_num = int(len(net_worths) * 0.9)
    for i in range(total_num):
        index = indices[i]
        tup = (ages[index], net_worths[index], diff[index])
        cleaned_data.append(tup)
    
    return cleaned_data

