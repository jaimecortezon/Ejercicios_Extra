#Implementa y prueba una función llamada elementos_mayores que tome una matriz de NumPy y un número n como argumentos. La función debe devolver una nueva matriz que contenga solo los elementos mayores que n.

import numpy as np

def elementos_mayores(matriz, n):
    return matriz[matriz > n]

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n = 5
print(elementos_mayores(matriz, n))



