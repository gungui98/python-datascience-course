import numpy as np

import numpy as np

def calculate(list):
    if ( len(list) < 9 ):
        raise ValueError("List must contain nine numbers.")
    else: 

        m = np.array(list).reshape(3,3)
        f = m.flatten()

        mean_axis0 = np.mean(m, axis = 0, dtype = float).tolist()
        mean_axis1 = np.mean(m, axis = 1, dtype = float).tolist()
        mean_axis_flat = np.mean(f).tolist()

        var_axis0 = np.var(m, axis = 0, dtype = float).tolist()
        var_axis1 = np.var(m, axis = 1, dtype = float).tolist()
        var_axis_flat = np.var(f, dtype = float).tolist()

        sd_axis0 = np.std(m, axis = 0, dtype = float).tolist()
        sd_axis1 = np.std(m, axis = 1, dtype = float).tolist()
        sd_axis_flat = np.std(f, dtype = float).tolist()

        max_axis0 = np.max(m, axis = 0).tolist()
        max_axis1 = np.max(m, axis = 1).tolist()
        max_axis_flat = np.max(f).tolist()

        min_axis0 = np.min(m, axis = 0).tolist()
        min_axis1 = np.min(m, axis = 1).tolist()
        min_axis_flat = np.min(f).tolist()

        sum_axis0 = np.sum(m, axis = 1, dtype = float).tolist()
        sum_axis1 = np.sum(m, axis = 0, dtype = float).tolist()
        sum_axis_flat = np.sum(f, dtype = float).tolist()

        calculations = {
            'mean': [mean_axis0,mean_axis1,mean_axis_flat],
            'variance': [var_axis0,var_axis1,var_axis_flat],
            'standard deviation': [sd_axis0,sd_axis1,sd_axis_flat],
            'max': [max_axis0,max_axis1,max_axis_flat],
            'min': [min_axis0,min_axis1,min_axis_flat],
            'sum': [sum_axis0,sum_axis1,sum_axis_flat]
         }



    return calculations