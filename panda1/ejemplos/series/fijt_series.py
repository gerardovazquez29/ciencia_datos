
import pandas as pd

calificaciones = pd.Series([10, 8, None, 6, 9, 10, 7, None, 5], name="calificacion")
print(calificaciones)
""" 
0    10.0
1     8.0
2     NaN
3     6.0
4     9.0
5    10.0
6     7.0
7     NaN
8     5.0
Name: calificacion, dtype: float64 
"""
print('_'*30)
calificaciones_sin_na = calificaciones.dropna()
print(calificaciones_sin_na)
""" 
0    10.0
1     8.0
3     6.0
4     9.0
5    10.0
6     7.0
8     5.0
Name: calificacion, dtype: float64 
"""
print('_'*30)
# Filtrado en Serie
# Quiero calificaciones ≥ 8:
calificaciones_buenas = calificaciones_sin_na[calificaciones_sin_na >= 8]
print(calificaciones_buenas)
""" 
0    10.0
1     8.0
4     9.0
5    10.0
Name: calificacion, dtype: float64 
"""
print('_'*30) 

# Quiero calificaciones entre 6 y 9:
calificaciones_entre_6_9 = calificaciones_sin_na[(calificaciones_sin_na >= 6) & (calificaciones_sin_na <= 9)]
print(calificaciones_entre_6_9)
""" 
1    8.0
3    6.0
4    9.0
6    7.0
Name: calificacion, dtype: float64 
"""
print('_'*30)

""" 
Tips:

Las condiciones van entre corchetes.
Combina condiciones con & (y) y | (o). 
"""
