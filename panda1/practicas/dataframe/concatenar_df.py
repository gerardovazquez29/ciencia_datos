import pandas as pd

ventas_enero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 
                             'Cantidad': [300, 200, 150]})

ventas_febrero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 
                               'Cantidad': [350, 210, 170]})

ventas_total = pd.concat([ventas_enero,ventas_febrero],ignore_index=True)
print(ventas_total)
"""
   Producto  Cantidad
0  Manzanas       300
1   Bananas       200
2  Naranjas       150
3  Manzanas       350
4   Bananas       210
5  Naranjas       170
"""
print('-'*30)

datos_cliente = pd.DataFrame({'Nombre': ["Ana", "Luis", "Marta"],
                               'Edad': [34, 45, 28]})
compras_cliente = pd.DataFrame({'Producto': ["Libro", "Lápiz", "Cuaderno"],
                                 'Precio': [15.50, 0.50, 2.00]})

info_clientes = pd.concat([datos_cliente,compras_cliente],axis=1)
print(info_clientes)
"""
   Nombre  Edad  Producto  Precio
0    Ana    34     Libro    15.5
1   Luis    45     Lápiz     0.5
2  Marta    28  Cuaderno     2.0 
"""
print('-'*30)

tienda_a = pd.DataFrame({'Producto': ["Manzanas", "Bananas"], 'Cantidad': [500, 300]})
tienda_b = pd.DataFrame({'Producto': ["Naranjas", "Peras"], 'Cantidad': [400, 250]})

ventas_tienda = pd.concat([tienda_a,tienda_b],keys=['Tienda A','Tienda B'])
print(ventas_tienda)
"""
            Producto  Cantidad
Tienda A 0  Manzanas       500
         1   Bananas       300
Tienda B 0  Naranjas       400
         1     Peras       250 
"""
print('-'*30)
