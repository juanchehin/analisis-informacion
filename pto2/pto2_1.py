# Vincular todas las tablas descargadas respecto a las entidades (sociedades)
# utilizando claves comunes como el nombre de la entidad o el CUIT.
#Listar al menos 50 registros resultantes de esta vinculación.

import pandas as pd

# cargar los archivos descargados
registro_sociedades = pd.read_csv("C:/dev/analisis-informacion/files/registro-nacional-sociedades-202409.csv")
igj = pd.read_csv("C:/dev/analisis-informacion/files/igj-entidades-202409.csv")
condicion_tributaria = pd.read_csv("C:/dev/analisis-informacion/files/SELE-SAL-CONSTA.csv")

# unir la primera tabla con la segunda usando cuit
df_merged = pd.merge(registro_sociedades, igj, on="cuit", how="inner")

# unir la tabla resultante con la tercera tabla
df_final = pd.merge(df_merged, condicion_tributaria, on="cuit", how="inner")

# listar
print(df_final.head(50))  # Imprime los primeros 50 registros

# guardar el archivo
df_final.to_excel("C:/dev/analisis-informacion/files/datos_vinculados.xlsx", index=False)
