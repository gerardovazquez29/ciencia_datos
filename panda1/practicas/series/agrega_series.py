import pandas as pd

numeros = pd.Series([10,20,30,40,50])
print(numeros)

promedio = numeros.mean()
print(f'E promedio es {promedio}') # 30.0

suma_total = numeros.sum()
print(suma_total) # 150

num_maximo = numeros.max()
print(num_maximo) # 50

num_minimo = numeros.min()
print(num_minimo) # 10


# Lista de edades
edades = pd.Series([23, 30, 26, 27, 22, 24, 25, 28])
promedio_edades = edades.mean()
print(f'El promedio de las edades es {promedio_edades}')
# El promedio de las edades es 25.625
print('-'*30)

# ventas
ventas = [120, 150, 90, 200, 210, 130, 160]
semana_ventas = pd.Series(ventas,index=('lunes','Martes','Miercoles','Jueves',
                                        'Viernes','Sabado','Domingo'))
print(semana_ventas)
"""
lunes        120
Martes       150
Miercoles     90
Jueves       200
Viernes      210
Sabado       130
Domingo      160
dtype: int64 
"""
print('-'*30)
suma_total_ventas = semana_ventas.sum()
print(f'la suma total de ventas de la semana es: ${suma_total_ventas}')
# la suma total de ventas de la semana es: $1060
print('-'*30)

dia_mayores_vantas = semana_ventas.max()
print(f'El dia mayor de ventas es {dia_mayores_vantas}')
# El dia mayor de ventas es 210
print('-'*30)

promedio_ventas = semana_ventas.mean()
print(f'El promedio de las ventas es ${promedio_ventas}')
# El promedio de las ventas es $151.42857142857142
print('-'*30)


# Serie de ventas del mes
ventas_mes = pd.Series([220, 235, 260, 213, 202, 298, 265, 198, 220, 230, 
                        190, 215, 275, 222, 218, 245, 233, 210, 290, 210,
                        215, 220, 225, 230, 245, 250, 260, 270, 280, 295])

total_venta_mes = ventas_mes.sum()
print(total_venta_mes) #7139
print('-'*30)

dia_ventas_mas_bajas = ventas_mes.min()
print(dia_ventas_mas_bajas) # 190
print('-'*30) 

promedio_ventas_mes = ventas_mes.mean()
print(promedio_ventas_mes) # 237.96666666666667
print('-'*30)
