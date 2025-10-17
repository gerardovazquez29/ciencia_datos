import pandas as pd

df = pd.read_csv('C:\\Users\\T-City\\OneDrive\\Desktop\\ciencia_datos\\panda1\\Precipitaciones.csv')
print(df)
print('-'*30)
print(type(df)) # <class 'pandas.core.frame.DataFrame'>

print(df.head()) # imprime los primeros 5 o si le pones el numero veras esa cantidad
print('-'*30)
print(df.tail()) # imprime los ultimos 5
print('-'*30) 
print(df.shape) # (52,14) imprime la cantidad de columnas y filas
print('-'*30)
print(df.columns) # imprime el nombre de todas las columnas
""" 
Index(['region', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
       'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
       'anual'],
      dtype='object') 
"""
print('-'*30)
print(df.info()) # imprime la informacion
""" 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 52 entries, 0 to 51
Data columns (total 14 columns): 
#   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   region      52 non-null     object
 1   enero       52 non-null     float64
 2   febrero     52 non-null     float64
 3   marzo       52 non-null     float64
 4   abril       52 non-null     float64
 5   mayo        52 non-null     float64
 6   junio       52 non-null     float64
 7   julio       52 non-null     float64
 8   agosto      52 non-null     float64
 9   septiembre  52 non-null     float64
 10  octubre     52 non-null     float64
 11  noviembre   52 non-null     float64
 12  diciembre   52 non-null     float64
 13  anual       52 non-null     float64
dtypes: float64(13), object(1)
memory usage: 5.8+ KB
None
"""
print('-'*30) 
print(df.describe()) # imprime una descripcion o caracteristicas

print('-'*30)

serie = df['region']
print(serie.head())
""" 
0    A CORUNA
1    ALBACETE
2    ALICANTE
3     ALMERIA
4       ARABA
Name: region, dtype: object 
"""
print('-'*30)
