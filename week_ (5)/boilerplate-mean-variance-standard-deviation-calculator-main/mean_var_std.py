import numpy as np

def calculate(lis):
    if len(lis) != 9 :
        raise ValueError("List must contain nine numbers.")
    a = np.array(lis, dtype=float).reshape((3, 3))
    calculations = {
        'mean': [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean()],
        'variance': [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a)],
        'standard deviation': [a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std()],
        'max': [a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max()],
        'min': [a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min()],
        'sum': [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum()]
    }
    return calculations