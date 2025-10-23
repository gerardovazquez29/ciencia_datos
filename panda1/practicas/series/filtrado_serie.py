import pandas as pd

serie = pd.Series([5,10,15,20,25])
print(serie)
"""
0     5     
1    10     
2    15     
3    20     
4    25     
dtype: int64 
"""
print('-'*30)
filtro = serie > 15
serie_filtrada = serie[filtro]
print(serie_filtrada)
""" 
3    20
4    25
dtype: int64 
"""
print('-'*30)
print(filtro)
""" 
0    False
1    False
2    False
3     True
4     True
dtype: bool 
"""
print('-'*30)


serie2 = pd.Series(['Banana','pera','melon','manzana'])
print(serie2)
""" 
0     Banana
1       pera
2      melon
3    manzana
dtype: object 
"""
print('-'*30)
print(type(serie2))
# <class 'pandas.core.series.Series'>
print(type(serie2[0]))
# <class 'str'>
print('-'*30)
#print(dir(serie2))
print('-'*30)
#print(help(serie2.str))
print('-'*30)
filtro2 = serie2.str.contains('m')
print(filtro2)
""" 
0    False
1    False
2     True
3     True
dtype: bool 
"""
print('-'*30)
print(serie2[filtro2])
""" 
2      melon
3    manzana
dtype: object 
"""
