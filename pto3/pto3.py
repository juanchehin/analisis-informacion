# Listar las entidades con más socios relacionados: 
# Identificar y listar las entidades (sociedades) que tengan la mayor cantidad de socios asociados

import pandas as pd

# Cargar los datos de los socios (cambia la ruta del archivo según tu sistema)
registro_sociedades = pd.read_csv("C:/dev/analis_info/datos_vinculados.csv")

# Agrupar por CUIT_entidad o razón social y contar la cantidad de socios por entidad
socios_por_entidad = registro_sociedades.groupby('CUIT_entidad').size().reset_index(name='Cantidad_de_Socios')

# Ordenar las entidades por la cantidad de socios de mayor a menor
socios_por_entidad_ordenados = socios_por_entidad.sort_values(by='Cantidad_de_Socios', ascending=False)

# Listar las entidades con más socios (las primeras 10 o 50)
print(socios_por_entidad_ordenados.head(50))  # Muestra las 50 entidades con más socios
