import numpy as np


def calculate(arr):
  if len(arr) != 9:
    raise ValueError("List must contain nine numbers.")
  arr = np.array(arr)
  mat = arr.reshape(3, 3)
  calculations = {
    'mean':
    [list(np.mean(mat, axis=0)),
     list(np.mean(mat, axis=1)),
     arr.mean()],
    'variance':
    [list(np.var(mat, axis=0)),
     list(np.var(mat, axis=1)),
     arr.var()],
    'standard deviation':
    [list(np.std(mat, axis=0)),
     list(np.std(mat, axis=1)),
     arr.std()],
    'max': [list(np.max(mat, axis=0)),
            list(np.max(mat, axis=1)),
            arr.max()],
    'min': [list(np.min(mat, axis=0)),
            list(np.min(mat, axis=1)),
            arr.min()],
    'sum': [list(np.sum(mat, axis=0)),
            list(np.sum(mat, axis=1)),
            arr.sum()]
  }
  return calculations
