
import pandas as pd

ruta = 'C:\\Users\\T-City\\OneDrive\\Desktop\\ciencia_datos\\panda1\\ejercicios\\medallas.csv'
df = pd.read_csv(ruta)
print(df)
print('-'*30)
print(df.shape) # (93, 5)
print(df.head())
print('-'*30)
print(df.info())
print('-'*30)
print(df.describe())
print('-'*30)
print(df.columns)
 #Index(['Oro', 'Plata', 'Bronce', 'Total', 'Pais'], dtype='object')
print(df.index)
 # RangeIndex(start=0, stop=93, step=1)
print('-'*30)
print(type(df))
# <class 'pandas.core.frame.DataFrame'>
print('-'*30)
print(df.isnull().sum()) # suma los valores nulos y los muestra
""" 
Oro       28
Plata     24
Bronce    17
Total      0
Pais       0
dtype: int64 
"""
print('-'*30)

df.fillna(0,inplace=True)
print(df)
"""      
Oro  Plata  Bronce  Total          Pais
0    0.0    1.0     2.0      3     Argentina
1    0.0    2.0     2.0      4       Armenia
2   17.0    7.0    22.0     46     Australia
3    1.0    1.0     5.0      7       Austria
4    0.0    3.0     4.0      7    Azerbaijan
..   ...    ...     ...    ...           ...
88   0.0    1.0     0.0      1  Turkmenistan
89   2.0    1.0     1.0      4        Uganda
90   1.0    6.0    12.0     19       Ukraine
91   3.0    0.0     2.0      5    Uzbekistan
92   1.0    3.0     0.0      4     Venezuela

[93 rows x 5 columns] 
"""
print('-'*30)
df['Oro'] = df['Oro'].astype(int)
df['Plata'] = df['Plata'].astype(int)
df['Bronce'] = df['Bronce'].astype(int)
print(df)
"""     
Oro  Plata  Bronce  Total          Pais
0     0      1       2      3     Argentina
1     0      2       2      4       Armenia
2    17      7      22     46     Australia
3     1      1       5      7       Austria
4     0      3       4      7    Azerbaijan
..  ...    ...     ...    ...           ...
88    0      1       0      1  Turkmenistan
89    2      1       1      4        Uganda
90    1      6      12     19       Ukraine
91    3      0       2      5    Uzbekistan
92    1      3       0      4     Venezuela

[93 rows x 5 columns] 
"""
print('-'*30)

top_3_oro = df.sort_values('Oro', ascending=False).head(3)
print(top_3_oro)
"""     
Oro  Plata  Bronce  Total                        Pais
25   39     41      33    113   Estados Unidos de America
72   38     32      18     88  Republica Popular de China
46   27     14      17     58                       Japon 
"""
print('-'*30)
filtro = df['Total'] > 10
mas_de_10_medallas = df[filtro]
mas_de_10_medallas.sort_values('Total', ascending=True)
print(mas_de_10_medallas)
"""    
Oro  Plata  Bronce  Total                        Pais
2    17      7      22     46                   Australia
11    7      6       8     21                      Brazil
14    7      6      11     24                      Canada
15    2      4       6     12              Chinese Taipei
19    7      3       5     15                        Cuba
20    4      4       3     11              Czech Republic
21    3      4       4     11                     Denmark
25   39     41      33    113   Estados Unidos de America
30    1     12      11     33                      France
32    1     11      16     37                     Germany
34   22     21      22     65                Gran Bretana
46   27     14      17     58                       Japon
60    1     12      14     36                 Netherlands
66    4      5       5     14                      Poland
72   38     32      18     88  Republica Popular de China
73    2     28      23     71                         ROC
81    3      8       6     17                       Spain
83    3      4       6     13                 Switzerland
87    2      2       9     13                      Turkey
90    1      6      12     19                     Ukraine 
"""
print('-'*30)

