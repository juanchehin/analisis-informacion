# Listar las entidades con más socios relacionados: 
# Identificar y listar las entidades (sociedades) que tengan la mayor cantidad de socios asociados

import pandas as pd

# cargar los datos
registro_sociedades = pd.read_excel("C:/dev/analisis-informacion/files/archivos_unidos.xlsx")

# agrupar por CUIT_entidad y contar la cantidad de socios por entidad
socios_por_entidad = registro_sociedades.groupby('cuit').size().reset_index(name='Cantidad_de_Socios')

# ordenar las entidades por la cantidad de socios de mayor a menor
socios_por_entidad_ordenados = socios_por_entidad.sort_values(by='Cantidad_de_Socios', ascending=False)

# listar
print(socios_por_entidad_ordenados.head(50))
