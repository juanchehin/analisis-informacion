# Vincular todas las tablas descargadas respecto a las entidades (sociedades)
# utilizando claves comunes como el nombre de la entidad o el CUIT.
#Listar al menos 50 registros resultantes de esta vinculación.

import pandas as pd

# cargar el archivo
registro_sociedades = pd.read_csv(
    "C:/dev/analisis-informacion/files/registro-nacional-sociedades-202409_recortado.csv",
    sep=',',
    quotechar='"',
    skipinitialspace=True
)

# cargar igj
igj = pd.read_csv(
    "C:/dev/analisis-informacion/files/igj-entidades-202409_recortado.csv",
    sep=',',
    quotechar='"',
    skipinitialspace=True,
    encoding='utf-8'
)

# cargar
sele_sal_consta = pd.read_csv(
    "C:/dev/analisis-informacion/files/SELE-SAL-CONSTA.csv",
    sep=',',
    quotechar='"',
    skipinitialspace=True,
    encoding='utf-8'
)

# limpiar los nombres de las columnas
registro_sociedades.columns = registro_sociedades.columns.str.strip()
igj.columns = igj.columns.str.strip()
sele_sal_consta.columns = sele_sal_consta.columns.str.strip()

# asegurarse de que 'cuit' existe
if 'cuit' not in registro_sociedades.columns:
    print("La columna 'cuit' no está en registro_sociedades")
if 'cuit' not in igj.columns:
    print("La columna 'cuit' no está en igj")
if 'cuit' not in sele_sal_consta.columns:
    print("La columna 'cuit' no está en SELE-SAL-CONSTA")

# unit los DataFrames si la columna 'cuit' está presente
if 'cuit' in registro_sociedades.columns and 'cuit' in igj.columns and 'cuit' in sele_sal_consta.columns:

    df_merged = pd.merge(registro_sociedades, igj, on="cuit", how="inner")
    
    df_merged_final = pd.merge(df_merged, sele_sal_consta, on="cuit", how="inner")
    
    # listar
    print(df_merged_final.head(50))

    # save
    df_merged_final.to_excel("C:/dev/analisis-informacion/files/datos_vinculados_final.xlsx", index=False)
else:
    print("No se puede realizar la fusión, ya que 'cuit' no está presente en todos los DataFrames.")
