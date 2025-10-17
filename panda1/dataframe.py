import pandas as pd

df_empleados = pd.DataFrame({
    'nombre': ['Ana','Luis','Carlos'],
    'edad': [30,25,40]
})
print(df_empleados)
"""
    nombre  edad
0     Ana    30
1    Luis    25
2  Carlos    40 
"""
print('-'*30)

edades = df_empleados['edad']
print(edades)
"""
0    30
1    25
2    40 
Name: edad, dtype: int64
"""
print('-'*30)

print(type(edades))
#<class 'pandas.core.series.Series'>
print('-'*30)

shape_df = df_empleados.shape
print(shape_df) # (3, 2) imprime la cantidad de columnas y filas

columns_df = df_empleados.columns
print(columns_df) # Index(['nombre', 'edad'], dtype='object')
# imprime el nombre de todas las columnas
index_df = df_empleados.index
print(index_df) # RangeIndex(start=0, stop=3, step=1)

print('-'*30)
