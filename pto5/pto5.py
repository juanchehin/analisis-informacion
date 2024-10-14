# Listar direcciones que cuenten con más entidades: 
# Identificar y listar las direcciones físicas que alberguen la mayor cantidad de entidades registradas

import pandas as pd

# cargar los datos de las entidade
entidades = pd.read_csv("C:/dev/analis_info/datos_vinculados.csv")

# concatear las columnas de direccion fiscal en una sola columna
entidades['direccion_fiscal'] = (entidades['dom_fiscal_calle'].astype(str) + " " +
                                 entidades['dom_fiscal_numero'].astype(str) + " " +
                                 entidades['dom_fiscal_piso'].astype(str) + " " +
                                 entidades['dom_fiscal_departamento'].astype(str) + ", " +
                                 entidades['dom_fiscal_localidad'].astype(str) + ", " +
                                 entidades['dom_fiscal_provincia'].astype(str))

# agrupar por la direccion concatenada y contar cuantas entidades estan en cada una
entidades_por_direccion = entidades.groupby('direccion_fiscal').size().reset_index(name='Cantidad_de_Entidades')

# ordenar las direcciones por la cantidad de entidades de mayor a menor
entidades_por_direccion_ordenadas = entidades_por_direccion.sort_values(by='Cantidad_de_Entidades', ascending=False)

# listar las direcciones con más entidades
print(entidades_por_direccion_ordenadas.head(50))