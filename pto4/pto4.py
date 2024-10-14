# Listar los socios con más entidades relacionadas: 
# Identificar y listar las personas físicas o jurídicas que estén relacionadas con el mayor número de entidades (sociedades)

import pandas as pd

# Cargar los datos de los socios (cambia la ruta del archivo según sea necesario)
registro_sociedades = pd.read_csv("datos_vinculados.csv")

# Agrupar por CUIT_socio (identificador del socio) y contar cuántas entidades tiene asociadas
entidades_por_socio = registro_sociedades.groupby('CUIT_socio').size().reset_index(name='Cantidad_de_Entidades')

# Ordenar los socios por la cantidad de entidades de mayor a menor
entidades_por_socio_ordenados = entidades_por_socio.sort_values(by='Cantidad_de_Entidades', ascending=False)

# Listar los socios con más entidades relacionadas (primeros 10 o 50)
print(entidades_por_socio_ordenados.head(50))  # Muestra los 50 socios con más entidades relacionadas
