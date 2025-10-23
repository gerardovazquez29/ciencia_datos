import pandas as pd

libros = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'titulo': ['El Quijote', 'La Odisea', 'Cien Años de Soledad', 'El Principito']
})

autores = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'nombre': ['Miguel de Cervantes', 'Homero', 'Gabriel García Márquez', 'J.K. Rowling']
})

libros_autores = pd.merge(libros,autores,on='ID',how='outer')
print(libros_autores)
"""
    ID                titulo                  nombre
0   1            El Quijote     Miguel de Cervantes
1   2             La Odisea                  Homero
2   3  Cien Años de Soledad  Gabriel García Márquez
3   4         El Principito                     NaN
4   5                   NaN            J.K. Rowling 
"""
print('-'*30)

cursos = pd.DataFrame({
    'curso_id': [101, 102, 103],
    'nombre_curso': ['Introducción a Python', 'Data Science con Python', 'Machine Learning Avanzado']
})

inscripciones = pd.DataFrame({
    'curso_id': [102, 102, 101, 104],
    'fecha_inscripcion': ['2023-01-15', '2023-02-01', '2023-01-20', '2023-03-05']
})

cursos_inscripciones = pd.merge(inscripciones,cursos,on='curso_id',how='right')
print(cursos_inscripciones)
"""
    curso_id fecha_inscripcion               nombre_curso
0       101        2023-01-20      Introducción a Python
1       102        2023-01-15    Data Science con Python
2       102        2023-02-01    Data Science con Python
3       103               NaN  Machine Learning Avanzado 
"""
print('-'*30)
cursos_inscripciones = pd.merge(inscripciones,cursos,on='curso_id',how='left')
print(cursos_inscripciones)
"""
    curso_id fecha_inscripcion             nombre_curso
0       102        2023-01-15  Data Science con Python
1       102        2023-02-01  Data Science con Python
2       101        2023-01-20    Introducción a Python
3       104        2023-03-05                      NaN 
"""
print('-'*30)

productos = pd.DataFrame({
    'ID': [10, 11, 12],
    'Nombre': ['Teclado', 'Mouse', 'Monitor'],
    'Marca': ['Logitech', 'Razer', 'Dell']
})

reviews = pd.DataFrame({
    'ID': [10, 11, 12],
    'Calificación': [5, 4, 4],
    'Comentario': ['Excelente producto', 'Buen producto', 'Satisfecho']
})

productos_reviews = pd.merge(productos,reviews,on='ID',how='inner')
print(productos_reviews)
"""
    ID   Nombre     Marca  Calificación          Comentario
0  10  Teclado  Logitech             5  Excelente producto
1  11    Mouse     Razer             4       Buen producto
2  12  Monitor      Dell             4          Satisfecho 
"""
print('-'*30)
productos_reviews = pd.merge(productos,reviews,left_index=True,right_index=True)
print(productos_reviews)
"""
    ID_x   Nombre     Marca  ID_y  Calificación          Comentario
0    10  Teclado  Logitech    10             5  Excelente producto
1    11    Mouse     Razer    11             4       Buen producto
2    12  Monitor      Dell    12             4          Satisfecho 
"""
print('-'*30)
