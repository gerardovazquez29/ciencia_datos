import pandas as pd

datos = [10,20,30,40,50]
serie1 = pd.Series(datos)
print(serie1)
print('-'*30)

indices = ['a','b','c','d','e']
serie1 = pd.Series(datos,indices)
print(serie1) 
# crea con las dos listas un tipo de diccionario con clave valor ahora indice

print('-'*30)

print(serie1['b']) # 20
print('-'*30)
print(type(serie1)) # <class 'pandas.core.series.Series'>
print(type(serie1['b'])) # <class 'numpy.int64'>
print('-'*30)

capitales = {'España':'Madrid','Peru':'Lima','Argentina':'Buenos Aires'}
serie2 = pd.Series(capitales)
print(serie2)
""" 
España             Madrid
Peru                 Lima
Argentina    Buenos Aires
dtype: object 
"""
print('-'*30)
print(serie2['Peru']) # Lima
print('-'*30)

serie_desde_diccionario = pd.Series({'a':30,'b':70,'c':160,'d':50})
sum_add = serie_desde_diccionario.loc[['a','d']].sum()
print(sum_add)  # 80  imprime el numero de a + d
print('-'*30)

numeros_serie = pd.Series([10,20,30,40,50])
numeros_serie.iloc[0] += 10
print(numeros_serie) # suma 10 ala primera posision
print('-'*30)

serie_1 = pd.Series([1, 2, 3, 6])
serie_2 = pd.Series([5, 6, 7, 5])
serie_sumada = serie_1 + serie_2
print(serie_sumada) # suma ambas series 
""" 
0     6
1     8
2    10
3    11
dtype: int64 
"""
print('-'*30) 

num1 = pd.Series([4,5,6])
num2 = pd.Series([8,9,10,2])
sum_listas = num1.add(num2,fill_value=0).astype(int)# convierte en integer
print(sum_listas) 
# suma las dos listas y al valor faltante le añade 0  
""" 
0    12
1    14
2    16
3     2 
dtype: int64
"""
super_serie = pd.Series(range(1,11))
valor = super_serie.iloc[8]
print(f'Valor en la posicion 8: {valor}') # Valor en la posicion 8: 9
raiz_cuadrada = int(super_serie.iloc[8] ** 0.5) # int convierte a integer 
print(raiz_cuadrada) # 3