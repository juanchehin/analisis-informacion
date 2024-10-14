# Vincular todas las tablas descargadas respecto a las entidades (sociedades)
# utilizando claves comunes como el nombre de la entidad o el CUIT.
#Listar al menos 50 registros resultantes de esta vinculación.


import pandas as pd

# Cargar los archivos descargados
registro_sociedades = pd.read_csv("C:/dev/analis_info/registro-nacional-sociedades-202409.csv")
igj = pd.read_csv("C:/dev/analis_info/igj-entidades-202409.csv")
condicion_tributaria = pd.read_csv("C:/dev/analis_info/SELE-SAL-CONSTA.csv")

# unir la primera tabla con la 2da usando CUIT
df_merged = pd.merge(registro_sociedades, igj, on="CUIT", how="inner")

# unir la tabla resultante con la 3er tabla
df_final = pd.merge(df_merged, condicion_tributaria, on="CUIT", how="inner")

# listar los primeros 50 registros
print(df_final.head(50))

# guardar el DataFrame en un excel
df_final.to_excel("datos_vinculados.xlsx", index=False)
