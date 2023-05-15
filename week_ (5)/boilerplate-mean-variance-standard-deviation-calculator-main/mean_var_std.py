import numpy as np

def calculate(list):
    if len(list)!=9:
      raise ValueError('List must contain nine numbers.')
    else:
      matrix = np.array(list).reshape(3,3)
    
    meanl = [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist()), (matrix.flatten().mean())]
    varl = [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()), (matrix.flatten().var())]
    stdl = [(matrix.std(axis=0).tolist()), (matrix.std(axis=1).tolist()), (matrix.flatten().std())]
    maximum = [(matrix.max(axis=0).tolist()), (matrix.max(axis=1).tolist()), (matrix.flatten().max())]
    minimum = [(matrix.min(axis=0).tolist()), (matrix.min(axis=1).tolist()), (matrix.flatten().min())]
    suml = [(matrix.sum(axis=0).tolist()), (matrix.sum(axis=1).tolist()), (matrix.flatten().sum())]

    calculations = {
      "mean": meanl,
      "variance": varl,
      "standard deviation": stdl,
      "max": maximum,
      "min": minimum,
      "sum": suml,
    }

    return calculations