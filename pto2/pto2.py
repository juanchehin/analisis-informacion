# Vincular todas las tablas descargadas respecto a las entidades (sociedades)
# utilizando claves comunes como el nombre de la entidad o el CUIT.
#Listar al menos 50 registros resultantes de esta vinculación.

import pandas as pd

# ========================================================
# *** union de archivos (previo tratamiento con openrefine) ***
# ========================================================
# Cargar los tres archivos Excel
df1 = pd.read_excel('C:/dev/analisis-informacion/files/SELE-SAL-CONSTA-recortado-csv.xlsx')
df2 = pd.read_excel('C:/dev/analisis-informacion/files/igj-entidades-202408-csv.xlsx')
df3 = pd.read_excel('C:/dev/analisis-informacion/files/registro-nacional-sociedades-202409-recortado-csv.xlsx')


df1['cuit'] = df1['cuit'].astype(str)
df2['cuit'] = df2['cuit'].astype(str)
df3['cuit'] = df3['cuit'].astype(str)

# Unir
merged_df = pd.merge(df1, df2, on='cuit', how='outer')
merged_df = pd.merge(merged_df, df3, on='cuit', how='outer')

# guardar el resultado en un nuevo archivo Excel
merged_df.to_excel('C:/dev/analisis-informacion/files/archivos_unidos.xlsx', index=False)

# listar
print(merged_df.head(50))
