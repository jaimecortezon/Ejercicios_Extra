#Escribe una función normalizar que reciba una matriz de NumPy y un modo. Y normalice la matriz dependiendo del modo de las siguientes maneras:
#Para normalizar se suma el valor absoluto mayor de los elementos negativos y se divide por el elemento mayor del resultado de la suma.
#Defecto: normaliza en general sobre toda la matriz.
#Columnas: normaliza cada columna por separado.
#Filas: normaliza cada fila por separado.
# Centrada_en_cero: Una vez normalizada se resta 0.5 a todos los valores para que el rango vaya de -0.5 a 0.5 con centro en cero.

import numpy as np

def normalizar(matriz, modo="Defecto"):
    if modo == "Defecto":
        return (matriz - matriz.min()) / (matriz.max() - matriz.min())
    elif modo == "Columnas":
        return (matriz - matriz.min(axis=0)) / (matriz.max(axis=0) - matriz.min(axis=0))
    elif modo == "Filas":
        return (matriz - matriz.min(axis=1)) / (matriz.max(axis=1) - matriz.min(axis=1))
    elif modo == "Centrada_en_cero":
        return (matriz - matriz.min()) / (matriz.max() - matriz.min()) - 0.5
    else:
        return "Modo no valido"
    
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(normalizar(matriz))
print(normalizar(matriz, "Columnas"))
print(normalizar(matriz, "Filas"))
print(normalizar(matriz, "Centrada_en_cero"))
print(normalizar(matriz, "Modo no valido"))



