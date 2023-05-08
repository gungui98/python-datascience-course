import numpy as np
 
def calculate(list):
    list = list [ : 9]
    if len(list) != 9: 
      raise ValueError("List must contain nine numbers.")
    if len(list) == 9:
      arr = np.reshape(list, (3,3))
 
      Mean0 = np.mean(arr, axis = 0). tolist()
      Mean1 = np.mean(arr, axis = 1).tolist()
      Mean = np.mean(arr)
 
      Variance0 = np.var(arr, axis = 0).tolist()
      Variance1 = np.var(arr, axis = 1).tolist()
      Variance = np.var(arr)
 
      StandardDeviation0 = np.nanstd(arr, axis = 0).tolist()
      StandardDeviation1 = np.nanstd(arr, axis = 1).tolist()
      StandardDeviation = np.nanstd(arr)
 
      Max0 = np.max(arr, axis = 0).tolist()
      Max1 = np.max(arr, axis = 1).tolist()
      Max = np.max(arr)
 
      Min0 = np.min(arr, axis = 0).tolist()
      Min1 = np.min(arr, axis = 1).tolist()
      Min = np.min(arr)
 
      Sum0 = np.sum(arr, axis = 0).tolist()
      Sum1 = np.sum(arr, axis = 1).tolist()
      Sum = np.sum(arr)
 
      calculations = {
        'mean': [Mean0, Mean1, Mean],
        'variance': [Variance0, Variance1, Variance],
        'standard deviation': [StandardDeviation0, StandardDeviation1, StandardDeviation],
        'max': [Max0, Max1, Max],
        'min': [Min0, Min1, Min],
        'sum': [Sum0, Sum1, Sum],
      }
 
      return calculations