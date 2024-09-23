import numpy as np

# Paso 1: Crear arrays con datos de ventas mensuales

months=np.array(["jan", "feb", "march", "april", "may", "jun", "jul", "agu", "sep", "oct", "nov", "dec"])
print("los meses son:")
print(months)

product_A=np.array(range(40, 150 + 1,10))
print("the product A")
print(product_A)

product_B = np.array(range(10, 120 + 1,10))
print("the  product B") 
print(product_B)   

print("efectivamente, la longitud del array es de ")
print(len(product_B))             

print("la suma de las ventas anuales de ambos prodcutos")

sum_A=sum(product_A)
sum_B=sum(product_B)
print(sum_A)
print(sum_B)

print("la suma de la venta anual ambos productos es")
venta_total=sum_A + sum_B
print(venta_total)
# Paso 2: Transformaciones básicas con NumPy
# Estadísticas básicas

#saquele la media de las ventas del producto de A y la media de las  ventas del producto B

print("la media anual de las ventas de A es")
media_A=np.mean(product_A)
print(media_A)

media_B = np.mean(product_B)
print("la media anual de las ventas de B es", media_B)

# Paso 3: Manipulación y análisis de datos
# Calcular el total de ventas por mes

ventas_mes=product_A + product_B
print("la venta total por mes es", ventas_mes)

# Calcular el promedio de ventas por producto
promedio_venta_producto =np.mean([media_A, media_B])
print("el promedio del promedio de ventas  ",promedio_venta_producto)

# Identificar el mes con mayor y menor ventas

#la venta más grande del producto A

venta_max_A= max(product_A)
print("la mayor venta de A es", venta_max_A)

venta_max_B = max(product_B)
print("la mayor venta de B es ", venta_max_B)

mes_mayor_venta_A =np.argmax(product_A)
print("el mayor mes para la venta de A es ", mes_mayor_venta_A)

mes_mayor_ventas_A = months[np.argmax(product_A)]
print("el mayor mes con ventas de A es", mes_mayor_ventas_A)
mes_mayor_ventas_B = months[np.argmax(product_B)]
print("el mayor mes con ventas de B es ", mes_mayor_ventas_B)