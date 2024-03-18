# Proyecto de medio curso
# Huella de carbono
# Fecha: 3/18/2024

# Importamos las librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leemos el archivo de datos
ruta = 'proyecto-mod1-sic'
derivados = '\derivados'
ruta_2 = ruta + derivados
data_og = ruta + '\owid-co2-data.csv'
data_og = pd.read_csv(data_og)

#___________________________________________Dataframe con los datos de 1990 en adelante_______________________________________

# Eliminamos las filas correspondientes a 1989 para atrás y guardamos en otro archivo nuevo
data = data_og[data_og['year'] > 1989]
data.to_csv(ruta_2 + '\owid-co2-data-1990.csv', index=False)



#___________________________________________Dataframe con los paises que nos interesan_______________________________________


# Creamos un nuevo dataframe con los paises que nos interesan
# United States, Canada, Japan, Germany, United Kingdom, China, India, Mexico, South Korea
data = data[(data['country'] == 'United States') | (data['country'] == 'Canada') | (data['country'] == 'Japan')|
            (data['country'] == 'Germany') | (data['country'] == 'United Kingdom') | (data['country'] == 'China')|
            (data['country'] == 'India') | (data['country'] == 'Mexico') | (data['country'] == 'South Korea')]


# Eliminamos las categorias con valores nulos
data_columns = data.columns
data = data.dropna(how='any', axis=1)
data_columns_new = data.columns
data.to_csv(ruta_2 + '\owid-co2-data-1990-country.csv', index=False)

print(f'Las categorias eliminadas son: {set(data_columns) - set(data_columns_new)}\n')



# ___________________________________________Dataframe con los paises industrializados y emergentes_______________________________________

# Separo los datos en dos grupos
# Paises industrializados: United States, Canada, Japan, Germany, United Kingdom
# Paises emergentes: China, India, Mexico, South Korea

data_ind = data[(data['country'] == 'United States') | (data['country'] == 'Canada') | (data['country'] == 'Japan')
                | (data['country'] == 'Germany') | (data['country'] == 'United Kingdom')]

data_em = data[(data['country'] == 'China') | (data['country'] == 'India') | (data['country'] == 'Mexico')
                | (data['country'] == 'South Korea')]


data_ind.to_csv(ruta_2 + '\industrializados.csv', index=False)
data_em.to_csv(ruta_2 + '\emergentes.csv', index=False)



# Las variables resultantantes son:
#   data_og: dataframe con los datos originales
#   data: dataframe con los datos de 1990 en adelante
#   data_ind: dataframe con los paises industrializados
#   data_em: dataframe con los paises emergentes

# Las categorias que se eliminaron son:


