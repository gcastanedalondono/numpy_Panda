import numpy as np

# Paso 1: Crear arrays con datos de ventas mensuales

months=np.array(["jan", "feb", "march", "april", "may", "jun", "jul", "agu", "sep", "oct", "nov", "dec"])


product_A=np.array(range(40, 150 + 1,10))

product_B = np.array(range(10, 120 + 1,10))


product_C= np.array([342, 23, 249, 12, 1400, 345, 12, 56, 67, 86, 39, 124])


ventas_matrix =np.array([months, product_A, product_B, product_C])
print(ventas_matrix)
la_trans =ventas_matrix.T
print("la transpuesta es", la_trans)
print(len(ventas_matrix))

