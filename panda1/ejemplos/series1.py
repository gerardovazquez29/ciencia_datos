import pandas as pd

# Creamos una Serie con tus frutas favoritas
# Esto es como tener una lista de colores de tus juguetes
frutas_favoritas = pd.Series(['Manzana', 'Plátano', 'Naranja', 'Uva'])

# Imprimimos la Serie original
print("Serie de Frutas Favoritas:")
print(frutas_favoritas)
""" 
Serie de Frutas Favoritas:
0    Manzana
1    Plátano
2    Naranja
3        Uva
dtype: object 
"""
print('-'*30)
# Agregamos una nueva fruta a la Serie
# Esto es como añadir un nuevo color a tu lista de colores
# Podemos usar .at para añadir un elemento en un índice específico
frutas_favoritas.at[4] = 'Fresa'

# Imprimimos la Serie actualizada
print("\nSerie de Frutas Favoritas con nueva fruta:")
print(frutas_favoritas)
""" 
Serie de Frutas Favoritas con nueva fruta:
0    Manzana
1    Plátano
2    Naranja
3        Uva
4      Fresa
dtype: object
------------------------------ 
"""
print('-'*30)
# También podemos crear una nueva Serie y concatenarla
# Esto es como tener una lista de colores y luego otra lista pequeña, y las juntas
nuevas_frutas = pd.Series(['Mango','Pera'])
frutas_favoritas = pd.concat([frutas_favoritas,nuevas_frutas], ignore_index=True)

# Imprimimos la Serie después de concatenar
print("\nSerie de Frutas Favoritas después de concatenar:")
print(frutas_favoritas)
""" 
Serie de Frutas Favoritas después de concatenar:
0    Manzana
1    Plátano
2    Naranja
3        Uva
4      Fresa
5      Mango
6       Pera
dtype: object 
"""
