import pandas as pd

ruta = "C:\\Users\\T-City\\OneDrive\\Desktop\\ciencia_datos\\panda1\\ejercicios\\Top-Películas.csv"

top_peliculas = pd.read_csv(ruta)
print(top_peliculas)

top_ordenado = top_peliculas.sort_values(by='rating',ascending=False) # ordena valores
print(top_ordenado.head())
"""
   indice_global  indice_estricto                    título              director     año  duración  género  rating  metascore  recaudación(M)
0             0              0.0  The Shawshank Redemption        Frank Darabont  1994.0     142.0   Drama     9.3       82.0           28.34 
1             1              1.0             The Godfather  Francis Ford Coppola  1972.0     175.0  Crimen     9.2      100.0          134.97 
2             2              1.0             The Godfather  Francis Ford Coppola  1972.0     175.0   Drama     9.2      100.0          134.97 
3             3              2.0           The Dark Knight     Christopher Nolan  2008.0     152.0  Acción     9.0       84.0          534.86 
4             4              2.0           The Dark Knight     Christopher Nolan  2008.0     152.0  Crimen     9.0       84.0          534.86  
"""
print('-'*30)
top_ordenado = top_peliculas.sort_values(by=['rating','recaudación(M)'],ascending=False)
print(top_ordenado.head(6))
"""
   indice_global  indice_estricto                    título              director     año  duración  género  rating  metascore  recaudación(M)
0             0              0.0  The Shawshank Redemption        Frank Darabont  1994.0     142.0   Drama     9.3       82.0           28.34 
1             1              1.0             The Godfather  Francis Ford Coppola  1972.0     175.0  Crimen     9.2      100.0          134.97 
2             2              1.0             The Godfather  Francis Ford Coppola  1972.0     175.0   Drama     9.2      100.0          134.97 
3             3              2.0           The Dark Knight     Christopher Nolan  2008.0     152.0  Acción     9.0       84.0          534.86 
4             4              2.0           The Dark Knight     Christopher Nolan  2008.0     152.0  Crimen     9.0       84.0          534.86 
5             5              2.0           The Dark Knight     Christopher Nolan  2008.0     152.0   Drama     9.0       84.0          534.86 
"""
print('-'*30)

top_agrupado = top_peliculas.groupby('género')['rating'].mean()
print(top_agrupado)
"""
 género
Acción             7.987255
Animación          7.943902
Aventura           7.980435
Biografía          7.971698
Ciencia Ficción    7.986567
Comedia            7.909910
Crimen             7.993500
Deportes           7.980000
Drama              7.980444
Familiar           7.932692
Fantasía           7.929508
Film-Noir          7.977273
Guerra             8.053191
Historia           7.931818
Misterio           7.991262
Musica             7.909677
Musical            7.943750
Romance            7.937398
Terror             7.875758
Thriller           7.929286
Western            8.006250
Name: rating, dtype: float64 
"""
print('-'*30)

top_agrupado = top_peliculas.groupby('año')['recaudación(M)'].sum()
print(top_agrupado.sort_values(ascending=False).head())
"""
 año
2014.0    8015.90
2019.0    7092.95
2010.0    6899.96
2016.0    6860.23
2015.0    6817.12
Name: recaudación(M), dtype: float64 
"""
