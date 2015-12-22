""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):

    # empty array, return None
    if len(arr) == 0:
        return None

    # all the elements are the same, return [1,1,1,...]
    if arr.count(arr[0]) == len(arr):
        return [1]*len(arr)

    maxVal = max(arr)
    minVal = min(arr)
    lst = []
    for a in arr:
        aa = float(a - minVal) / (maxVal - minVal)
        lst.append(aa)

    return lst

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)

