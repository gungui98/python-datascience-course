import numpy as np

def calculate(list):
    if (len(list) < 9):
        raise ValueError("List must contain nine numbers.")
    array = np.array(list).reshape(3, 3)
    
    listmean = [array.mean(axis = 0).tolist(), array.mean(axis = 1).tolist(), array.mean()]
    listvar = [array.var(axis = 0).tolist(), array.var(axis = 1).tolist(), array.var()]
    liststd = [array.std(axis = 0).tolist(), array.std(axis = 1).tolist(), array.std()]
    listmax = [array.max(axis = 0).tolist(), array.max(axis = 1).tolist(), array.max()]
    listmin = [array.min(axis = 0).tolist(), array.min(axis = 1).tolist(), array.min()]
    listsum = [array.sum(axis = 0).tolist(), array.sum(axis = 1).tolist(), array.sum()]
    
    calculations = {
        'mean': listmean ,
        'variance': listvar ,
        'standard deviation': liststd,
        'max': listmax,
        'min': listmin,
        'sum': listsum
    }
    
    return calculations