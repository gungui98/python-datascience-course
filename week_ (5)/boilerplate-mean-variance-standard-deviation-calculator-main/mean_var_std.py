import numpy as np

def calculate(mylist):
    mylist = mylist[:9]
    if(len(mylist) !=9 ):
        raise ValueError('List must contain nine numbers.')
    a = np.array(mylist).reshape((3,3))
    calculations = {
        'mean': [list(np.mean(a,axis = 0)),list(np.mean(a,axis = 1)),np.mean(a)],
        'variance': [list(np.var(a,axis = 0)),list(np.var(a,axis = 1)),np.var(a)],
        'standard deviation': [list(np.std(a,axis = 0)),list(np.std(a,axis = 1)),np.std(a)],
        'max': [list(np.max(a,axis = 0)),list(np.max(a,axis = 1)),np.max(a)],
        'min': [list(np.min(a,axis = 0)),list(np.min(a,axis = 1)),np.min(a)],
        'sum': [list(np.sum(a,axis = 0)),list(np.sum(a,axis = 1)),np.sum(a)],
    }
    return calculations