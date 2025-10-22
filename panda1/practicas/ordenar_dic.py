import pandas as pd

datos = {
    'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D'],
    'año': [2001, 2000, 2005, 2010],
    'rating': [7.2, 6.5, 8.1, 7.5]
}
df_peliculas = pd.DataFrame(datos)
print(df_peliculas)
"""
        titulo   año  rating
0  Pelicula A  2001     7.2
1  Pelicula B  2000     6.5
2  Pelicula C  2005     8.1
3  Pelicula D  2010     7.5 
"""
print('-'*30)
df_ordenado = df_peliculas.sort_values(by='año')
print(df_ordenado)
"""
        titulo   año  rating
1  Pelicula B  2000     6.5
0  Pelicula A  2001     7.2
2  Pelicula C  2005     8.1
3  Pelicula D  2010     7.5 
"""
print('-'*30)

df_ordenado = df_peliculas.sort_values(by=['rating','año'],ascending=[False,True])
print(df_ordenado)
"""
       titulo   año  rating
2  Pelicula C  2005     8.1
3  Pelicula D  2010     7.5
0  Pelicula A  2001     7.2
1  Pelicula B  2000     6.5
"""
print('-'*30)

datos1 = {
    'titulo': ['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D', 'Pelicula E'],
    'género': ['Acción', 'Drama', 'Acción', 'Comedia', 'Drama'],
    'rating': [7.2, 8.5, 9.1, 6.5, 7.8]
}
df_pelix = pd.DataFrame(datos1)
print(df_pelix)
"""_summary_
       titulo   género  rating
0  Pelicula A   Acción     7.2
1  Pelicula B    Drama     8.5
2  Pelicula C   Acción     9.1
3  Pelicula D  Comedia     6.5
4  Pelicula E    Drama     7.8
"""
print('-'*30)
promedio_rating_por_genero = df_pelix.groupby('género')['rating'].mean()
print(promedio_rating_por_genero)
"""_summary_
género
Acción     8.15
Comedia    6.50
Drama      8.15
Name: rating, dtype: float64
"""
print('-'*30)

