# Proyecto de medio curso para Samsung Innovation Campus: Huella de carbono

# Lectura de datos y limpieza
# Autor: Dwight Sutherland
# Fecha: 3/18/2024



#______________________________________Resumen de los cambios y variables resultantes_______________________________________
'''
Este codigo se encarga de limpiar los datos originales y de crear un nuevo dataframe con los datos de 1990 en adelante.
Ademas, se crea un dataframe con los paises que nos interesan y se separan en dos grupos: paises industrializados 
y paises emergentes.

Para cada uno de los dataframes se crea un archivo csv para su visualizacion rapida y se crea un codebook con las 
definiciones de las categorias restantes.

Los archivos creados por este código son:

    - owid-co2-data-1990.csv: dataframe con los datos de 1990 en adelante
    - owid-co2-data-1990-country.csv: dataframe con los paises que nos interesan
    - industrializados.csv: dataframe con los paises industrializados
    - emergentes.csv: dataframe con los paises emergentes
    - owid-co2-codebook-new.csv: codebook con las categorias restantes
'''



# Las variables resultantes son:
#   data_og: dataframe con los datos originales
#   data: dataframe con los datos de 1990 en adelante
#   data_ind: dataframe con los paises industrializados
#   data_em: dataframe con los paises emergentes
#   codebook_og: codebook original
#   codebook: codebook con las categorias restantes



# Las categorias que se eliminaron porque incluían datos vacios son:
'''
{'cumulative_other_co2', 'share_of_temperature_change_from_ghg', 'temperature_change_from_n2o', 'trade_co2_share', 
'energy_per_gdp', 'consumption_co2_per_capita', 'methane', 'temperature_change_from_ch4', 'consumption_co2', 
'ghg_excluding_lucf_per_capita', 'co2_including_luc_per_gdp', 'co2_per_gdp', 'trade_co2', 'gdp', 'nitrous_oxide', 
'temperature_change_from_ghg', 'temperature_change_from_co2', 'share_global_other_co2', 'consumption_co2_per_gdp', 
'methane_per_capita', 'share_global_cumulative_other_co2', 'total_ghg_excluding_lucf', 'ghg_per_capita', 
'nitrous_oxide_per_capita', 'total_ghg', 'other_industry_co2', 'other_co2_per_capita'}
'''
#

# Las categorias que permanecen son:
'''
{'co2_including_luc', 'cumulative_coal_co2', 'flaring_co2', 'oil_co2', 'coal_co2', 'coal_co2_per_capita', 
'land_use_change_co2', 'year', 'share_global_cement_co2', 'share_global_cumulative_coal_co2', 'energy_per_capita', 
'share_global_cumulative_cement_co2', 'share_global_gas_co2', 'cumulative_flaring_co2', 'oil_co2_per_capita', 
'co2_per_unit_energy', 'share_global_flaring_co2', 'iso_code', 'co2_including_luc_growth_prct', 'co2', 
'cumulative_cement_co2', 'population', 'share_global_cumulative_co2_including_luc', 'gas_co2_per_capita', 
'share_global_cumulative_co2', 'co2_per_capita', 'share_global_cumulative_flaring_co2', 'share_global_coal_co2', 
'share_global_co2_including_luc', 'cement_co2_per_capita', 'cumulative_co2_including_luc', 'cumulative_gas_co2', 
'co2_including_luc_per_unit_energy', 'share_global_luc_co2', 'share_global_oil_co2', 'share_global_co2', 'gas_co2', 
'primary_energy_consumption', 'cement_co2', 'co2_growth_abs', 'country', 'share_global_cumulative_oil_co2', 
'share_global_cumulative_gas_co2', 'flaring_co2_per_capita', 'co2_including_luc_per_capita', 
'co2_including_luc_growth_abs', 'cumulative_oil_co2', 'land_use_change_co2_per_capita', 
'share_global_cumulative_luc_co2', 'cumulative_luc_co2', 'co2_growth_prct', 'cumulative_co2'}
'''



#________________________________________________________________________________________#
#___________________________________________Codigo_______________________________________#
#________________________________________________________________________________________#



### Importamos las librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#___________________________________________Lectura de los datos_______________________________________

### Leemos el archivo de datos
ruta = 'proyecto-mod1-sic'      # Ruta donde se encuentra el archivo
derivados = '\derivados'        # Ruta donde se guardaran los archivos creados
ruta_2 = ruta + derivados       # Ruta completa
data_og = ruta + '\owid-co2-data.csv'
data_og = pd.read_csv(data_og)      # Dataframe con los datos originales



#___________________________________________Dataframe con los datos de 1990 en adelante_______________________________________
### Eliminamos las filas correspondientes a 1989 para atrás y guardamos en otro archivo nuevo

data = data_og[data_og['year'] > 1989]      # Dataframe con los datos de 1990 en adelante
data.to_csv(ruta_2 + '\data-1990.csv', index=False)



#___________________________________________Dataframe con los paises que nos interesan_______________________________________
'''
Creamos un nuevo dataframe con los paises que nos interesan
United States, Canada, Japan, Germany, United Kingdom, China, India, Mexico, South Korea
'''

data = data[(data['country'] == 'United States') | (data['country'] == 'Canada') | (data['country'] == 'Japan')|
            (data['country'] == 'Germany') | (data['country'] == 'United Kingdom') | (data['country'] == 'China')|
            (data['country'] == 'India') | (data['country'] == 'Mexico') | (data['country'] == 'South Korea')]


### Eliminamos las categorias con valores nulos
data_columns = data.columns
data = data.dropna(how='any', axis=1)       # Eliminamos las categorias con valores nulos
data_columns_new = data.columns
data.to_csv(ruta_2 + '\data-1990-country_of_interest.csv', index=False)

'''print(f'Las categorias eliminadas son: {set(data_columns) - set(data_columns_new)}\n')
print(f'Las categorias que permanecen son: {set(data_columns_new)}\n')'''



# ___________________________________________Dataframe con los paises industrializados y emergentes_______________________________________

'''
Separo los datos en dos grupos:
    - Paises industrializados: United States, Canada, Japan, Germany, United Kingdom
    - Paises emergentes: China, India, Mexico, South Korea
'''

### Dataframe con los paises industrializados
data_ind = data[(data['country'] == 'United States') | (data['country'] == 'Canada') | (data['country'] == 'Japan')
                | (data['country'] == 'Germany') | (data['country'] == 'United Kingdom')]

### Dataframe con los paises emergentes
data_em = data[(data['country'] == 'China') | (data['country'] == 'India') | (data['country'] == 'Mexico')
                | (data['country'] == 'South Korea')]


data_ind.to_csv(ruta_2 + '\industrializados.csv', index=False)
data_em.to_csv(ruta_2 + '\emergentes.csv', index=False)



#___________________________________________Codebook con las categorias restantes_______________________________________

### Modificacion del codebook para que permanezcan solo las categorias restantes
codebook_og = pd.read_csv(ruta + '\owid-co2-codebook.csv')     
codebook = codebook_og[codebook_og['column'].isin(data_columns_new)]      
codebook.to_csv(ruta_2 + '\codebook-new.csv', index=False)

# print(f'El nuevo codebook tiene {len(codebook)} categorias\nEL codebook original tiene {len(data_columns)} categorias\n')