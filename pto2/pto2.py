# Vincular todas las tablas descargadas respecto a las entidades (sociedades)
# utilizando claves comunes como el nombre de la entidad o el CUIT.
#Listar al menos 50 registros resultantes de esta vinculación.


import pandas as pd

# Cargar los archivos descargados
registro_sociedades = pd.read_csv("C:/dev/analisis-informacion/files/registro-nacional-sociedades-202409_recortado.csv")
igj = pd.read_csv("C:/dev/analisis-informacion/files/igj-entidades-202409_recortado.csv")
condicion_tributaria = pd.read_csv("C:/dev/analisis-informacion/files/SELE-SAL-CONSTA_recortado.csv")

# unir la primera tabla con la 2da usando CUIT
df_merged = pd.merge(registro_sociedades, igj, on="CUIT", how="inner")

# unir la tabla resultante con la 3er tabla
df_final = pd.merge(df_merged, condicion_tributaria, on="CUIT", how="inner")

# listar los primeros 50 registros
print(df_final.head(50))

# guardar el DataFrame en un excel
df_final.to_excel("C:/dev/analisis-informacion/files/datos_vinculados.xlsx", index=False)
