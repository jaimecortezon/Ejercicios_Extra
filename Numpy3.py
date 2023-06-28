#Escribe una función estandarizar que reciba una matriz de NumPy y un modo. Y estandarice la matriz dependiendo del modo de las siguientes maneras:
#Para estandarizar se debe restar la media de los valores y dividir por la desviación estándar.
#Defecto: estandariza en general sobre toda la matriz.
#Columnas: estandariza cada columna por separado.
#Filas: estandariza cada fila por separado.

import numpy as np

def estandarizar(matriz, modo="Defecto"):
    if modo == "Defecto":
        return (matriz - matriz.mean()) / matriz.std()
    elif modo == "Columnas":
        return (matriz - matriz.mean(axis=0)) / matriz.std(axis=0)
    elif modo == "Filas":
        return (matriz - matriz.mean(axis=1)) / matriz.std(axis=1)
    else:
        return "Modo no valido"
    
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(estandarizar(matriz))
print(estandarizar(matriz, "Columnas"))
print(estandarizar(matriz, "Filas"))
print(estandarizar(matriz, "Modo no valido"))

