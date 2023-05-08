import numpy as np

def calculate(list):
    if(len(L) != 9 ):
        raise ValueError("List must contain nine numbers.")
    L = np.array(L).reshape((3,3))

    calculations = {
    'mean':[list(np.mean(L,axis=0)) , list(np.mean(L,axis=1)),np.mean(L)],
    'variance':[list(np.var(L,axis=0)) , list(np.var(L,axis=1)),np.var(L)],
    'standard deviation':[list(np.std(L,axis=0)) , list(np.std(L,axis=1)),np.std(L)],
    'max':[list(np.max(L,axis=0)) , list(np.max(L,axis=1)),np.max(L)],
    'min':[list(np.min(L,axis=0)) , list(np.min(L,axis=1)),np.min(L)],
    'sum':[list(np.sum(L,axis=0)) , list(np.sum(L,axis=1)),np.sum(L)],
    
    
  }
 
  
    return calculations