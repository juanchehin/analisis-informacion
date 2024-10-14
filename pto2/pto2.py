# Vincular todas las tablas descargadas respecto a las entidades (sociedades)
# utilizando claves comunes como el nombre de la entidad o el CUIT.
#Listar al menos 50 registros resultantes de esta vinculación.


import pandas as pd

# Cargar los archivos descargados
registro_sociedades = pd.read_csv("C:/dev/analis_info/registro-nacional-sociedades-202409.csv")
igj = pd.read_csv("C:/dev/analis_info/igj-entidades-202409.csv")
condicion_tributaria = pd.read_csv("C:/dev/analis_info/SELE-SAL-CONSTA.csv")

# 1. Unir la primera tabla (Registro Nacional de Sociedades) con la segunda (IGJ) usando CUIT
df_merged = pd.merge(registro_sociedades, igj, on="CUIT", how="inner")

# 2. Luego, unir la tabla resultante con la tercera tabla (Condición Tributaria)
df_final = pd.merge(df_merged, condicion_tributaria, on="CUIT", how="inner")

# 3. Listar los primeros 50 registros resultantes
print(df_final.head(50))  # Imprime los primeros 50 registros

# 4. Guardar el DataFrame final en un archivo Excel
df_final.to_excel("datos_vinculados.xlsx", index=False)  # Guarda el DataFrame en un archivo Excel
