import numpy as np

def calculate(lst):
  if (len(lst) != 9):
    raise ValueError("List must contain nine numbers.")
  arr = np.array([lst[:3:], lst[3:6:], lst[6::]])
  ans = {
    'mean': [[arr[:, j].mean() for j in range(3)], [i.mean() for i in arr], np.mean(lst)],
    'variance': [[arr[:, j].var() for j in range(3)], [i.var() for i in arr], np.var(lst)],
    'standard deviation': [[arr[:, j].std() for j in range(3)], [i.std() for i in arr], np.std(lst)],
    'max': [[arr[:, j].max() for j in range(3)], [i.max() for i in arr], np.max(lst)],
    'min': [[arr[:, j].min() for j in range(3)], [i.min() for i in arr], np.min(lst)],
    'sum': [[arr[:, j].sum() for j in range(3)], [i.sum() for i in arr], np.sum(lst)],
  }
  return ans
