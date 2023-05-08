import numpy as np


def calculate(list):
      if len(list) != 9:
        raise ValueError( "List must contain nine numbers.")
  
      mat = np.array(
        [np.array(list[0:3]),
         np.array(list[3:6]),
         np.array(list[6:9])])
  

          meanAx1 = mat.mean(axis=0).tolist()
          meanAx2 = mat.mean(axis=1).tolist()
          meanOva = mat.mean().tolist()

        varAx1 = mat.var(axis=0).tolist()
        varAx2 = mat.var(axis=1).tolist()
        varOva = mat.var().tolist()

        stdAx1 = mat.std(axis=0).tolist()
        stdAx2 = mat.std(axis=1).tolist()
        stdOva = mat.std().tolist()

        maxAx1 = mat.max(axis=0).tolist()
        maxAx2 = mat.max(axis=1).tolist()
        maxOva = mat.max().tolist()

        minAx1 = mat.min(axis=0).tolist()
        minAx2 = mat.min(axis=1).tolist()
        minOva = mat.min().tolist()

        sumAx1 = mat.sum(axis=0).tolist()
        sumAx2 = mat.sum(axis=1).tolist()
        sumOva = mat.sum().tolist()

        calculations = {
            'mean': [meanAx1, meanAx2, meanOva],
            'variance': [varAx1, varAx2, varOva],
            'standard deviation': [stdAx1, stdAx2, stdOva],
            'max': [maxAx1, maxAx2, maxOva],
            'min': [minAx1, minAx2, minOva],
            'sum': [sumAx1, sumAx2, sumOva]
        }
  
  

      return calculations
