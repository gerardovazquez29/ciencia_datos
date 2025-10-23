import pandas as pd

datos = {
    "Titulo": ["El Quijote", "Cien años de soledad", "La odisea"],
    "Autor": ["Miguel de Cervantes", "Gabriel García Márquez", "Homero"],
    "Año": [1605, 1967, -800]
}
libros_df = pd.DataFrame(datos)
print(libros_df)
"""
                  Titulo                   Autor   Año
0            El Quijote     Miguel de Cervantes  1605
1  Cien años de soledad  Gabriel García Márquez  1967
2             La odisea                  Homero  -800 
"""
print('-'*30)
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sara'],
    'Edad': [25, 30, 22, 27],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Bilbao']
}
df = pd.DataFrame(data)
print(df)
"""
    Nombre  Edad     Ciudad    
0     Ana    25     Madrid
1    Luis    30  Barcelona
2  Carlos    22   Valencia
3    Sara    27     Bilbao 
"""
print('-'*30)
#df_filtrados = df[df['Edad'] > 25]
edades = df['Edad']
df_filtrados = df[edades > 25]
print(df_filtrados)
print('-'*30)
"""
   Nombre  Edad     Ciudad
1   Luis    30  Barcelona
3   Sara    27     Bilbao 
"""
df["edad_en_10_años"] = df["Edad"] + 10
print(df)
"""
     Nombre  Edad     Ciudad  edad_en_10_años
0     Ana    25     Madrid               35
1    Luis    30  Barcelona               40
2  Carlos    22   Valencia               32
3    Sara    27     Bilbao               37 
"""
print('-'*30)
df_ciudades = df['Ciudad'].str.upper()
print(df_ciudades)
"""
0       MADRID
1    BARCELONA
2     VALENCIA
3       BILBAO
Name: Ciudad, dtype: object 
"""
print('-'*30)
df["es_mayor_de_25"] = df["Edad"] > 25
print(df)
"""
    Nombre  Edad     Ciudad  edad_en_10_años  es_mayor_de_25
0     Ana    25     Madrid               35           False
1    Luis    30  Barcelona               40            True
2  Carlos    22   Valencia               32           False
3    Sara    27     Bilbao               37            True 
"""
print('-'*30)
 