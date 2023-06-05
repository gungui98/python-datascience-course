import numpy as np

def calculate(list):
    if (len(list) < 9):
        raise ValueError("List must contain nine numbers.")
    list_reshape = np.array(list).reshape((3,3))

    calculations = {
        "mean": [np.mean(list_reshape, axis = 0).tolist(), np.mean(list_reshape, axis = 1).tolist(), np.array(list).mean()],
        "variance": [np.var(list_reshape, axis = 0).tolist(), np.var(list_reshape, axis = 1).tolist(), np.array(list).var()],
        "standard deviation": [np.std(list_reshape, axis = 0).tolist(), np.std(list_reshape, axis = 1).tolist(), np.array(list).std()],
        "max": [np.max(list_reshape, axis = 0).tolist(), np.max(list_reshape, axis = 1).tolist(), np.array(list).max()],
        "min": [np.min(list_reshape, axis = 0).tolist(), np.min(list_reshape, axis = 1).tolist(), np.array(list).min()],
        "sum": [np.sum(list_reshape, axis = 0).tolist(), np.sum(list_reshape, axis = 1).tolist(), np.array(list).sum()]
    }
    return calculations