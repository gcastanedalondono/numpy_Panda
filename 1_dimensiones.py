#Manipular datos con multiples dimensiones
#Siempre debemos saber que dimensión son
#Las dimensiones estructuran datos para cálculos complejos e insigths valiosos
#Un escalar es dimension cero

import numpy as np
escalar = np.array(27)
print(type(escalar))
print(escalar)

vector =np.array([30, 29,32,35,37,38, 42])
print(vector)
print(type(vector))

#Para matrices
print("para matrices, en otros lenguajes las listas quedaban como algo derecho")
print("ya así quedan con el orden que es")
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)

print("Creando un tensor")
tensor=np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor)

print("Hay seis mecanicos generales para crear arrayas en numpy")
print(" el primero es conversión de otras estrucutras de datos como listas y tuplas")
print("La segunda son las funciones de creaciónd e arrayas de numpy, crear una matriz de cero")
print("la replicación, unión o mutación de arrays ")
print("lectura desde disco o medios personalizados")
print("creación de arrays desde bytes crudos")
print("uso de funciones especiales de bibliotecas")

print("usaremos un método de arange ")

array_arange=np.arange(10)
print(array_arange)

print("podemos crear la matriz identidad, pones la dimensión")
eye_matrix=np.eye(4)
print(eye_matrix)

print("también puede estar la matriz diagonal")
diag=np.diag([1,2,3])
print(diag)

print("método random")
random = np.random.random((2,3))
print(random)




