import pandas as pd

# Cargar los archivos descargados
registro_sociedades = pd.read_csv("registro-nacional-sociedades-202409.csv")
igj = pd.read_csv("igj-entidades-202409.csv")
condicion_tributaria = pd.read_csv("SELE-SAL-CONSTA.csv")

# 1. Unir la primera tabla (Registro Nacional de Sociedades) con la segunda (IGJ) usando CUIT
df_merged = pd.merge(registro_sociedades, igj, on="CUIT", how="inner")

# 2. Luego, unir la tabla resultante con la tercera tabla (Condición Tributaria)
df_final = pd.merge(df_merged, condicion_tributaria, on="CUIT", how="inner")

# 3. Listar los primeros 50 registros resultantes
print(df_final.head(50))  # Imprime los primeros 50 registros