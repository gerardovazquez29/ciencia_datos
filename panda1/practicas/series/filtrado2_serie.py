import pandas as pd

serie_numeros = pd.Series([n for n in range(1, 14)])
print(serie_numeros)
""" 
0      1
1      2
2      3
3      4
4      5
5      6
6      7
7      8
8      9
9     10
10    11
11    12
12    13
dtype: int64 
"""
print('-'*30)
serie_filtrada = serie_numeros > 10
filtro = serie_numeros[serie_filtrada]
print(filtro)
""" 
10    11
11    12
12    13
dtype: int64 
"""
print('-'*30)
valores = pd.Series([18, 22, 7, 9, 15, 8])
print('-'*30)
condicion_valores_pares = valores % 2 == 0
print(condicion_valores_pares)
""" 
0     True
1     True
2    False
3    False
4    False
5     True
dtype: bool 
"""
print('-'*30)
valores_pares = valores[condicion_valores_pares]
print(valores_pares)
""" 
0    18
1    22
5     8
dtype: int64 
"""
print('-'*30)


frutas = pd.Series(["manzana", "banana", "cereza", "durazno", "frambuesa"])
frutas_con_e = frutas.str.contains('e')
print(frutas_con_e)
""" 
0    False
1    False
2     True
3    False
4     True
dtype: bool 
"""
print('-'*30)
print(frutas[frutas_con_e])
""" 
2       cereza
4    frambuesa
dtype: object 
"""
print('-'*30)
