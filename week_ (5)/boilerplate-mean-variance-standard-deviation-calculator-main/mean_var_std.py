import numpy as np

def calculate(mylist):
    if len(mylist) != 9:
        raise ValueError('List must contain nine numbers.')
    mylist = np.reshape(mylist, (3,3))
    calculations = {
      'mean': [list(np.mean(mylist, axis = 0)), list(np.mean(mylist, axis = 1)), np.mean(mylist)],
      'variance': [list(np.var(mylist, axis = 0)), list(np.var(mylist, axis = 1)), np.var(mylist)],
      'standard deviation': [list(np.std(mylist, axis = 0)), list(np.std(mylist, axis = 1)), np.std(mylist)],
      'max': [list(np.max(mylist, axis = 0)), list(np.max(mylist, axis = 1)), np.max(mylist)],
      'min': [list(np.min(mylist, axis = 0)), list(np.min(mylist, axis = 1)), np.min(mylist)],
      'sum': [list(np.sum(mylist, axis = 0)), list(np.sum(mylist, axis = 1)), np.sum(mylist)]
    }
    return calculations