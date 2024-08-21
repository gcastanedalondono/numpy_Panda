print("La indexación y slicing, permiten trabajar subconjuntos para evitar trabajar sobre la totalidad de datos")
import numpy as np
array= np.array([10, 20, 30, 40, 50])
print("el primer segundo elemento")
print(array[1])
print("el último elemento")
print(array[-1])

print("podemos acceder a subconjuntos utilizando variable[1:1]")
print(array[0:4])

print("si excedo el valor del número de elementos, él solo me mostrará hasta el último elemento")
print(array[0:8])

print(array[-1:-7])
print("Permite hacer la indexación booleana, hacer una consulta de qué valores están bajo cierta condición ")

print("para ver qué elementos cumplen una condición")
bool_index = array > 25
print(bool_index)
print(type(bool_index))

index = [2,0,4]
print(array[index])


