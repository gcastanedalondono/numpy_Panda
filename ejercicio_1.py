import numpy as np

# Paso 1: Crear arrays con datos de ventas mensuales

months=np.array(["jan", "feb", "march", "april", "may", "jun", "jul", "agu", "sep", "oct", "nov", "dec"])
print("los meses son:")
print(months)

product_A=np.random.randint(40,100, size=(1,12))
print("the product A")
print(product_A)

product_B = list(range(10, 120 + 1,10))
print("the  product B") 
print(product_B)   

print("efectivamente, la longitud del array es de 12")
print(len(product_B))             
