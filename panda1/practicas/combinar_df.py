import pandas as pd

# Creación del DataFrame df_a
df_a = pd.DataFrame({
    'id': [1, 2, 3],
    'Nombre': ['Ana', 'Beto', 'Carla']
})
df_a.set_index('id', inplace=True)

# Creación del DataFrame df_b
df_b = pd.DataFrame({
    'id': [1, 2, 3],
    'Edad': [25, 30, 35]
})
df_b.set_index('id', inplace=True)

df_combinado = df_a.join(df_b)
print(df_combinado)
"""
    Nombre  Edad
id
1     Ana    25
2    Beto    30
3   Carla    35 
"""
print('-'*30)

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
}).set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2],
    'NombreCategoria': ['Categoría 1', 'Categoría 2']
}).set_index('CategoriaID')

df_combinado1 = productos_df.join(categorias_df,how='left')
print(df_combinado1)
"""
                 Nombre  Precio NombreCategoria
ProductoID
1           Producto 1     100     Categoría 1
2           Producto 2     150     Categoría 2
3           Producto 3     200             NaN
4           Producto 4     250             NaN 
"""
print('-'*30)

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
})
productos_df = productos_df.set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2, 3],
    'NombreCategoria': ['Categoría 1', 'Categoría 2', 'Categoría 3']
}).set_index('CategoriaID')

df_combinado2 = categorias_df.join(productos_df,how='right')
print(df_combinado2)
"""
            NombreCategoria      Nombre  Precio
ProductoID
1              Categoría 1  Producto 1     100
2              Categoría 2  Producto 2     150
3              Categoría 3  Producto 3     200
4                      NaN  Producto 4     250 
"""
print('-'*30)

