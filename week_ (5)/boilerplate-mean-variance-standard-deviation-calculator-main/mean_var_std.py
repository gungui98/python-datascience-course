import numpy as np

def calculate(llist):
    if len(llist) != 9: raise ValueError("List must contain nine numbers.")
    llist = np.array(llist)
    mat = llist.reshape(3, 3)
    calculations = {
        'mean': [list(np.mean(mat, axis = 0)), list(np.mean(mat, axis = 1)), llist.mean()],
        'variance': [list(np.var(mat, axis = 0)), list(np.var(mat, axis = 1)), llist.var()],
        'standard deviation': [list(np.std(mat, axis = 0)), list(np.std(mat, axis = 1)), llist.std()],
        'max': [list(np.max(mat, axis = 0)), list(np.max(mat, axis = 1)), llist.max()],
        'min': [list(np.min(mat, axis = 0)), list(np.min(mat, axis = 1)), llist.min()],
        'sum': [list(np.sum(mat, axis = 0)), list(np.sum(mat, axis = 1)), llist.sum()]
    }
    return calculations