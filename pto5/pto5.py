# Listar direcciones que cuenten con más entidades: 
# Identificar y listar las direcciones físicas que alberguen la mayor cantidad de entidades registradas

import pandas as pd

# Cargar los datos de las entidades (cambia la ruta del archivo según tu sistema)
entidades = pd.read_csv("datos_vinculados.csv")

# Concatenar las columnas de dirección fiscal en una sola columna para simplificar el análisis
entidades['direccion_fiscal'] = (entidades['dom_fiscal_calle'].astype(str) + " " +
                                 entidades['dom_fiscal_numero'].astype(str) + " " +
                                 entidades['dom_fiscal_piso'].astype(str) + " " +
                                 entidades['dom_fiscal_departamento'].astype(str) + ", " +
                                 entidades['dom_fiscal_localidad'].astype(str) + ", " +
                                 entidades['dom_fiscal_provincia'].astype(str))

# Agrupar por la dirección concatenada y contar cuántas entidades están en cada una
entidades_por_direccion = entidades.groupby('direccion_fiscal').size().reset_index(name='Cantidad_de_Entidades')

# Ordenar las direcciones por la cantidad de entidades de mayor a menor
entidades_por_direccion_ordenadas = entidades_por_direccion.sort_values(by='Cantidad_de_Entidades', ascending=False)

# Listar las direcciones con más entidades (primeros 10 o 50)
print(entidades_por_direccion_ordenadas.head(50))  # Muestra las 50 direcciones con más entidades registradas
