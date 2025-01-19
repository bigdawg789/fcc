import numpy as np
import pandas as pd

def calculate(list):
    if len(list) != 9:
            raise ValueError("List must contain nine numbers.")
    a1, a2, a3, b1, b2, b3, c1, c2, c3 = list
    matrix = np.array([[a1, a2, a3],[b1, b2, b3],[c1, c2, c3]])

    mean = [arr.tolist() for arr in [np.mean(matrix,axis=0),np.mean(matrix,axis=1),np.mean(matrix.flatten())]]
    variance = [arr.tolist() for arr in[np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(matrix.flatten())]]
    std = [arr.tolist() for arr in[np.std(matrix, axis=0), np.std(matrix, axis=1), np.std(matrix.flatten())]]
    max = [arr.tolist() for arr in[np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(matrix.flatten())]]
    min = [arr.tolist() for arr in[np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(matrix.flatten())]]
    sum = [arr.tolist() for arr in[np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(matrix.flatten())]]
    result =  {'mean':mean, 'variance':variance, 'std':std, 'max':max, 'min':min, 'sum':sum}
    return result

list = [0,1,2,3,4,5,6,7,8]
print(calculate(list))
