import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5],
    'Producto': ['Producto A', 'Producto B', None, 'Producto D', 'Producto E'],
    'Cantidad': [10, 20, 30, None, 50],
    'Precio': [100, 200, 300, 400, None]
}
df = pd.DataFrame(data)
print(df)
"""
   ID    Producto  Cantidad  Precio
0   1  Producto A      10.0   100.0
1   2  Producto B      20.0   200.0
2   3        None      30.0   300.0
3   4  Producto D       NaN   400.0
4   5  Producto E      50.0     NaN 
"""
print('-'*30)
valores_nulos = df.isnull().sum()
print(valores_nulos)
""" 
ID          0
Producto    1
Cantidad    1
Precio      1
dtype: int64 
"""
print('-'*30)

datos = {
    'ID': [1, 2, 3, 4, 1],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto A'],
    'Cantidad': [10, 20, 30, 40, 50],
    'Precio': [100, 200, 300, 400, 100]
}
dfs = pd.DataFrame(datos)
print(dfs)
"""
    ID    Producto  Cantidad  Precio
0   1  Producto A        10     100
1   2  Producto B        20     200
2   3  Producto C        30     300
3   4  Producto D        40     400
4   1  Producto A        50     100 
"""
print('-'*30)
df_sin_duplicados = dfs.drop_duplicates(subset='ID')
#NOTA:en este caso al eliminar el duplicado del ID se eliminan las demas de su columna
print(df_sin_duplicados)
"""
    ID    Producto  Cantidad  Precio
0   1  Producto A        10     100
1   2  Producto B        20     200
2   3  Producto C        30     300
3   4  Producto D        40     400 
"""
print('-'*30)

datos1 = {
    'ID': [1, 2, 3, 4],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Cantidad': [10, 20, 30, 40],
    'Precio': [100, None, 300, None]
}
df1 = pd.DataFrame(datos1)
print(df1)
"""
    ID    Producto  Cantidad  Precio
0   1  Producto A        10   100.0
1   2  Producto B        20     NaN
2   3  Producto C        30   300.0
3   4  Producto D        40     NaN 
"""
print('-'*30)
precio_promedio = df1['Precio'].mean()
print(precio_promedio) # 200.0
print('-'*30)

df1['Precio'] = df1['Precio'].fillna(precio_promedio)
# remplaza los valores nulos en la columna Precio por el promedio
print(df1)
"""
    ID    Producto  Cantidad  Precio
0   1  Producto A        10   100.0
1   2  Producto B        20   200.0
2   3  Producto C        30   300.0
3   4  Producto D        40   200.0 
"""
print('-'*30)
