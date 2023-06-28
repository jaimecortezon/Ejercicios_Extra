#Escribe un programa que cargue el archivo “adultos.csv” en un array ten en cuenta que tiene encabezado por columna indicando el significado de cada una. Usando lo que hemos visto en clase calcula en este programa:
#el porcentaje de mujeres que tienen un ingreso superior a 50k anual.
#el porcentaje de hombres que tienen un ingreso superior a 50k anual.
#el porcentaje de personas blancas que tienen un ingreso superior a 50k anual.
#el porcentaje de personas negras que tienen un ingreso superior a 50k anual.
#el porcentaje de personas asiáticas que tienen un ingreso superior a 50k anual.
#el porcentaje de personas de otras razas que tienen un ingreso superior a 50k anual.
#el porcentaje de personas menores de 30 años que tienen ingreso superior a 50k anual.
#el porcentaje de personas entre 30 y 55 años que tienen ingreso superior a 50k anual.
#el porcentaje de personas mayores de 55 años que tienen ingreso superior a 50k anual.
#el porcentaje de personas con una educación igual o superior a 10 (educación universitaria) que tienen un ingreso superior a 50k anual.

import pandas as pd

# Cargar el archivo CSV en un DataFrame
data = pd.read_csv('adultos.csv')

# Calcular el total de personas
total_personas = len(data)

# 1. Porcentaje de mujeres con ingreso superior a 50k anual
mujeres_ingreso_superior = len(data[(data['income'] == '>50K') & (data['sex'] == 'Female')])
porcentaje_mujeres = (mujeres_ingreso_superior / total_personas) * 100

# 2. Porcentaje de hombres con ingreso superior a 50k anual
hombres_ingreso_superior = len(data[(data['income'] == '>50K') & (data['sex'] == 'Male')])
porcentaje_hombres = (hombres_ingreso_superior / total_personas) * 100

# 3. Porcentaje de personas blancas con ingreso superior a 50k anual
blancos_ingreso_superior = len(data[(data['income'] == '>50K') & (data['race'] == 'White')])
porcentaje_blancos = (blancos_ingreso_superior / total_personas) * 100

# 4. Porcentaje de personas negras con ingreso superior a 50k anual
negros_ingreso_superior = len(data[(data['income'] == '>50K') & (data['race'] == 'Black')])
porcentaje_negros = (negros_ingreso_superior / total_personas) * 100

# 5. Porcentaje de personas asiáticas con ingreso superior a 50k anual
asiaticos_ingreso_superior = len(data[(data['income'] == '>50K') & (data['race'] == 'Asian-Pac-Islander')])
porcentaje_asiaticos = (asiaticos_ingreso_superior / total_personas) * 100

# 6. Porcentaje de personas de otras razas con ingreso superior a 50k anual
otras_razas_ingreso_superior = len(data[(data['income'] == '>50K') & (data['race'] == 'Other')])
porcentaje_otras_razas = (otras_razas_ingreso_superior / total_personas) * 100

# 7. Porcentaje de personas menores de 30 años con ingreso superior a 50k anual
menores_30_ingreso_superior = len(data[(data['income'] == '>50K') & (data['age'] < 30)])
porcentaje_menores_30 = (menores_30_ingreso_superior / total_personas) * 100

# 8. Porcentaje de personas entre 30 y 55 años con ingreso superior a 50k anual
entre_30_55_ingreso_superior = len(data[(data['income'] == '>50K') & (data['age'].between(30, 55))])
porcentaje_entre_30_55 = (entre_30_55_ingreso_superior / total_personas) * 100

# 9. Porcentaje de personas mayores de 55 años con ingreso superior a 50k anual
mayores_55_ingreso_superior = len(data[(data['income'] == '>50K') & (data['age'] > 55)])
porcentaje_mayores_55 = (mayores_55_ingreso_superior / total_personas) * 100

# 10. Porcentaje de personas con una educación igual o superior a 10 (educación universitaria) con ingreso superior a 50k anual
educacion_superior_10_ingreso_superior = len(data[(data['income'] == '>50K') & (data['education-num'] >= 10)])
porcentaje_educacion_superior_10 = (educacion_superior_10_ingreso_superior / total_personas) * 100

















