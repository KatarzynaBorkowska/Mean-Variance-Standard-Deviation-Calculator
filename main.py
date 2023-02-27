import numpy as np

def calculate(axis):
    if len(axis) != 9:
        return "List must contain nine numbers."
    arr = np.array(axis)
    matrix = arr.reshape((3,3))
    return matrix

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))