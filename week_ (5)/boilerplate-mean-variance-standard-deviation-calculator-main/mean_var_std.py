import numpy as np

def calculate(mylist):
    mylist = mylist[:9]
    if (len(mylist) != 9):
        raise ValueError("List must contain nine numbers.")
    arr = np.array(mylist).reshape(3, 3)
    calculations = {
        'mean' : [
            list(np.mean(arr, axis=0)),
            list(np.mean(arr, axis=1)),
            np.mean(arr)
        ],

        'variance' : [
            list(np.var(arr, axis=0)),
            list(np.var(arr, axis=1)),
            np.var(arr)
        ],

        'standard deviation' : [
            list(np.std(arr, axis=0)),
            list(np.std(arr, axis=1)),
            np.std(arr)
        ],

        'max' : [
            list(np.max(arr, axis=0)),
            list(np.max(arr, axis=1)),
            np.max(arr)
        ],

        'min' : [
            list(np.min(arr, axis=0)),
            list(np.min(arr, axis=1)), 
            np.min(arr)
        ],

        'sum' : [
            list(np.sum(arr, axis=0)),
            list(np.sum(arr, axis=1)),
            np.sum(arr)
        ]
    }
    return calculations