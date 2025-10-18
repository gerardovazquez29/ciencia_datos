import pandas as pd


calificaciones = pd.Series([10, 8, None, 6, 9, 10, 7, None, 5], name="calificacion")

print(calificaciones)

print('-'*30)

calificaciones_sin_na = calificaciones.dropna()
print(calificaciones_sin_na)

print('-'*30)

# Agregación en Serie
# Estadísticos rápidos:

prom = calificaciones_sin_na.mean()
mediana = calificaciones_sin_na.median()
maximo = calificaciones_sin_na.max()
conteo = calificaciones_sin_na.count()
resumen = calificaciones_sin_na.describe()

""" 
Tips:

describe te da una vista general.
count ignora NaN por defecto. 
"""

