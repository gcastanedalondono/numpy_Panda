import numpy as np
print("para resolver sistemas de matrices es muy importante la transposición de matrices")
print("invertir arrays sirve para el procesamiento de señales")
print("la transposición es cambiar sus filas y columnas")

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
transposed_matrix=matrix.T 
print(matrix)
print(transposed_matrix)

Breslev= np.array([["HaShem", "Emunah", "simja"], [1,9,10]])
print(Breslev)
Breslev_T=Breslev.T
print(Breslev_T)

print("vamos a ver el reshape, para cambiar la forma de un array sin cambiar sus datos")
print("ojo se debe respetar el número de elemtos")


array = np.arange(1,13)
reshaped_array = array.reshape(3,4)
print(array)
print(reshaped_array)

print("en algoritmos métodos como el reverse que nos ayuda a voltearlos ")
reversed_array =array[::-1]
print(array)
print(reversed_array)

print("el flatering es volver un array multidimensional en un elemento de una dimensión")
matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
flattened_array = matrix.flatten()
print(matrix)
print(flattened_array)
print("esto se utiliza en deep learning para que lo que se toma de una pantalla pase por cada una de las neuronas")

