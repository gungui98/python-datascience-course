import numpy as np

def mean(nplist):
    '''
    Return the mean of a list in this format: [axis1, axis2, flattened]
    '''
    return [list(nplist.mean(axis=0)), list(nplist.mean(axis=1)), nplist.mean()]

def variance(nplist):
    '''
    Return the variance of a list in this format: [axis1, axis2, flattened]
    '''
    return [list(nplist.var(axis=0)), list(nplist.var(axis=1)), nplist.var()]

def standard_deviation(nplist):
    '''
    Return the standard deviation of a list in this format: [axis1, axis2, flattened]
    '''
    return [list(nplist.std(axis=0)), list(nplist.std(axis=1)), nplist.std()]

def max(nplist):
    '''
    Return the max of a list in this format: [axis1, axis2, flattened]
    '''
    return [list(nplist.max(axis=0)), list(nplist.max(axis=1)), nplist.max()]

def min(nplist):
    '''
    Return the min of a list in this format: [axis1, axis2, flattened]
    '''
    return [list(nplist.min(axis=0)), list(nplist.min(axis=1)), nplist.min()]

def sum(nplist):
    '''
    Return the sum of a list in this format: [axis1, axis2, flattened]
    '''
    return [list(nplist.sum(axis=0)), list(nplist.sum(axis=1)), nplist.sum()]


def calculate(list):
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")

    nplist = np.reshape(np.array(list), newshape=(3,3))

    return {'mean': mean(nplist),
            'variance': variance(nplist),
            'standard deviation': standard_deviation(nplist),
            'max': max(nplist),
            'min': min(nplist),
            'sum': sum(nplist)}

print(calculate([0,1,2,3,4,5,6,7,8]))