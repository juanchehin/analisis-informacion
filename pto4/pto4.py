# Listar los socios con más entidades relacionadas: 
# Identificar y listar las personas físicas o jurídicas que estén relacionadas con el mayor número de entidades (sociedades)

import pandas as pd

# cargar los datos
registro_sociedades = pd.read_csv("C:/dev/analisis-informacion/files/datos_vinculados.csv")

# agrupar por cuit del socio y contar cuantas entidades tiene asociadas
entidades_por_socio = registro_sociedades.groupby('cuit').size().reset_index(name='cantidad_entidades')

# ordenar los socios por la cantidad de entidades de mayor a menor
entidades_por_socio_ordenados = entidades_por_socio.sort_values(by='cantidad_entidades', ascending=False)

# listar
print(entidades_por_socio_ordenados.head(50))