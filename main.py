import numpy as np

def calculate(list):
    if len(list) != 9:
        return "List must contain nine numbers."
    arr = np.array(list)
    matrix = arr.reshape((3,3))
    wynik = {
        "mean": [ matrix.mean(axis=0).tolist(), matrix.mean(1).tolist() ,matrix.mean()],
        "variance": [np.var(matrix, 0).tolist(), np.var(matrix, 1).tolist(), np.var(matrix)]
    }
    return wynik

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))