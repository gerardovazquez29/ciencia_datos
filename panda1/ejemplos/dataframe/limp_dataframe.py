import pandas as pd

data = {'Id_producto': [1001,1002,1003,1003],
        'Cantidad_vendida': [30,None,25,25],
        'Precio': [20.5,15.0,None,22.5]}
df = pd.DataFrame(data)
print(df)
print('-'*30)
"""    
    Id_producto  Cantidad_vendida  Precio
0         1001              30.0    20.5
1         1002               NaN    15.0
2         1003              25.0     NaN
3         1003              25.0    22.5 
"""
# Exploracion 
print(df.head())
# importante imprime los primeros 5 de la tabla
print('-'*30)
print(df.info()) # imprime la informacion del dataframe
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
  
0   Id_producto       4 non-null      int64
 1   Cantidad_vendida  3 non-null      float64
 2   Precio            3 non-null      float64
dtypes: float64(2), int64(1)
memory usage: 228.0 bytes
None 
""" 
print('-'*30)

# Identificar Valores Faltantes (Nulos)
print(df.isnull()) # imprime los valores faltantes 
""" 
    Id_producto  Cantidad_vendida  Precio
0        False             False   False
1        False              True   False
2        False             False    True
3        False             False   False 
"""
print('-'*30)
print(df.isnull().sum()) # suma el valor flotante y lo muestra
""" 
Id_producto         0
Cantidad_vendida    1
Precio              1
dtype: int64 
"""
print('-'*30)

# Manejo de valores Faltantes
# opcion 1 eliminar los valores nulos
df_eliminados = df.dropna() # elimina los valores nulos
print(df_eliminados)
"""
    Id_producto  Cantidad_vendida  Precio
0         1001              30.0    20.5
3         1003              25.0    22.5 
"""
print('-'*30)
# opcion 2 remplazar los valores nulos con otros valores
valores_nuevos = {'Cantidad_vendida': 0, 'Precio':df['Precio'].mean()}
# mean() = saca el porcentaje del total de  todos los valores
df_rellenados = df.fillna(valores_nuevos).astype(int)
# cambio el tipo de valor antes era flot ahora es int
print(df_rellenados)
"""
    Id_producto  Cantidad_vendida  Precio
0         1001                30      20
1         1002                 0      15
2         1003                25      19
3         1003                25      22 
"""

print('-'*30)
# Eliminacion de Duplicados
df_unicos = df_rellenados.drop_duplicates(subset='Id_producto')
# Se eliminan los duplicados de la celda id_producto
print(df_unicos)
"""
    Id_producto  Cantidad_vendida  Precio
0         1001                30      20
1         1002                 0      15
2         1003                25      19 
"""
print('-'*30)
