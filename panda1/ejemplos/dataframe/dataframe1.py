import pandas as pd

# Creamos un diccionario con los datos de tus amigos
# Las "claves" del diccionario serán los nombres de las columnas
# Los "valores" serán listas con los datos de cada columna

datos_amigos = {
    'Nombre': ['Ana', 'Luis', 'Sofía', 'Pedro'],
    'Edad': [7, 8, 7, 9],
    'Juguete_Favorito': ['Muñeca', 'Carro', 'Peluche', 'Bloques']
}

# Creamos el DataFrame a partir del diccionario
# Esto es como organizar tus juguetes en la caja grande
df_amigos = pd.DataFrame(datos_amigos)
print("DataFrame de Amigos:")
print(df_amigos)
""" 
DataFrame de Amigos:
  Nombre  Edad Juguete_Favorito
0    Ana     7           Muñeca
1   Luis     8            Carro
2  Sofía     7          Peluche
3  Pedro     9          Bloques 
"""
print('-'*30)
# Agregamos una nueva columna al DataFrame
# Esto es como añadir una nueva categoría a tu caja de juguetes, por ejemplo, "Color_Favorito"

df_amigos['Color_Favorito'] = ['Rosa','Azul','Amarillo','Verde']
# Imprimimos el DataFrame actualizado
print("\nDataFrame de Amigos con nueva columna:")
print(df_amigos)
""" 
DataFrame de Amigos con nueva columna:
  Nombre  Edad Juguete_Favorito Color_Favorito
0    Ana     7           Muñeca           Rosa
1   Luis     8            Carro           Azul
2  Sofía     7          Peluche       Amarillo
3  Pedro     9          Bloques          Verde 
"""
print('-'*30)

# Agregamos una nueva fila al DataFrame
# Esto es como añadir un nuevo amigo a tu lista
# Primero creamos una nueva Serie con los datos del nuevo amigo

nuevo_amigo = pd.Series(['Elena',8,'Patineta','Morado'], index=df_amigos.columns)

# Usamos .loc para añadir la nueva fila. El número 4 es el índice de la nueva fila.
# Esto es como poner un nuevo juguete en la caja en un espacio específico
df_amigos.loc[4] = nuevo_amigo
# Imprimimos el DataFrame con la nueva fila
print("\nDataFrame de Amigos con nueva fila:")
print(df_amigos)
""" 
DataFrame de Amigos con nueva fila:
  Nombre  Edad Juguete_Favorito Color_Favorito
0    Ana     7           Muñeca           Rosa
1   Luis     8            Carro           Azul
2  Sofía     7          Peluche       Amarillo
3  Pedro     9          Bloques          Verde
4  Elena     8         Patineta         Morado
------------------------------ 
"""
print('-'*30)
