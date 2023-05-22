import numpy as np

def calculate(list):
    if len(list) != 9: raise ValueError('List must contain nine numbers.')
    else: npl= np.array(list).reshape((3,3))
    return {
        'mean': [np.mean(npl, axis=0).tolist(),np.mean(npl, axis=1).tolist(),np.mean(npl).tolist()],
        'variance': [np.var(npl, axis=0).tolist(),np.var(npl, axis=1).tolist(),np.var(npl).tolist()],
        'standard deviation': [np.std(npl, axis=0).tolist(),np.std(npl, axis=1).tolist(),np.std(npl).tolist()],
        'max': [np.max(npl, axis=0).tolist(),np.max(npl, axis=1).tolist(),np.max(npl).tolist()],
        'min': [np.min(npl, axis=0).tolist(),np.min(npl, axis=1).tolist(),np.min(npl).tolist()],
        'sum': [np.sum(npl, axis=0).tolist(),np.sum(npl, axis=1).tolist(),np.sum(npl).tolist()]
    }