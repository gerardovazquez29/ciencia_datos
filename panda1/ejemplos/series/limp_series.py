import pandas as pd


calificaciones = pd.Series([10,8,None,6,9,10,7,None,5], name='calificaciones')
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
Name: calificaciones, dtype: float64 
"""
print('-'*30)

# Limpieza en Serie

# Quitar valores faltantes (None/NaN):
# Opcion 1
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
Name: calificaciones, dtype: float64 
"""
print('-'*30)
# CONVERTIR CALIFICACIONES A ENTEROS

# Opción 1: Convertir después de eliminar NaN
calificaciones_int_opcion1 = calificaciones.dropna().astype(int)
print("Opción 1 - Eliminar NaN y convertir a int:")
print(calificaciones_int_opcion1)
print(f"Tipo de datos: {calificaciones_int_opcion1.dtype}")
""" 
Opción 1 - Eliminar NaN y convertir a int:
0    10
1     8
3     6
4     9
5    10
6     7
8     5
Name: calificaciones, dtype: int64
Tipo de datos: int64 
"""
print('-'*30)


# Rellenar valores faltantes:
# Opcion 2
calificaciones_fill = calificaciones.fillna(calificaciones.mean()) # usa el promedio para rellenar
print(calificaciones_fill)
""" 
0    10.000000
1     8.000000
2     7.857143
3     6.000000
4     9.000000
5    10.000000
6     7.000000
7     7.857143
8     5.000000
Name: calificaciones, dtype: float64 
"""
print('-'*30)
# Opción 2: Rellenar NaN con un valor y luego convertir a int
calificaciones_int_opcion2 = calificaciones.fillna(0).astype(int)
print("Opción 2 - Rellenar NaN con 0 y convertir a int:")
print(calificaciones_int_opcion2)
print(f"Tipo de datos: {calificaciones_int_opcion2.dtype}")
""" 
Opción 2 - Rellenar NaN con 0 y convertir a int:
0    10
1     8
2     0
3     6
4     9
5    10
6     7
7     0
8     5
Name: calificaciones, dtype: int64
Tipo de datos: int64 
"""
print('-'*30) 

# Detectar y recodificar valores fuera de rango (ej: calificación debe ser 0–10):
# Opcion 3
calificaciones_clip = calificaciones.clip(lower=0, upper=10)
print(calificaciones_clip)
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
Name: calificaciones, dtype: float64 
"""
print('-'*30)
# Opción 3: Usar nullable integer dtype (mantiene NaN como pd.NA)
calificaciones_int_opcion3 = calificaciones.astype('Int64')  # Nota la 'I' mayúscula
print("Opción 3 - Usar nullable integer (mantiene valores faltantes):")
print(calificaciones_int_opcion3)
print(f"Tipo de datos: {calificaciones_int_opcion3.dtype}")
""" 
Opción 3 - Usar nullable integer (mantiene valores faltantes):
0      10
1       8
2    <NA>
3       6
4       9
5      10
6       7
7    <NA>
8       5
Name: calificaciones, dtype: Int64
Tipo de datos: Int64 
"""
print('-'*30)
# Opción 4: Rellenar con la media y convertir a int
calificaciones_int_opcion4 = calificaciones.fillna(calificaciones.mean()).astype(int)
print("Opción 4 - Rellenar con la media y convertir a int:")
print(calificaciones_int_opcion4)
print(f"Tipo de datos: {calificaciones_int_opcion4.dtype}")
""" 
Opción 4 - Rellenar con la media y convertir a int:
0    10
1     8
2     7
3     6
4     9
5    10
6     7
7     7
8     5
Name: calificaciones, dtype: int64
Tipo de datos: int64 
"""
print('-'*30)

""" 
Tips:
Usa dropna para eliminar, fillna para completar.
clip te ayuda a “encarrilar” valores fuera de límites. 
"""



