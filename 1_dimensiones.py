#Manipular datos con multiples dimensiones
#Siempre debemos saber que dimensión son
#Las dimensiones estructuran datos para cálculos complejos e insigths valiosos
#Un escalar es dimension cero

import numpy as np
escalar = np.array(27)
print(type(escalar))
print(escalar)

#Pero queremos almacenar la temperatura de toda la semana
vector=np.array([30,29,31,34, 35, 36, 42 ])
print(vector)
#cuando son  de dimsesión dos, son matrices
matrix =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)

tensor =np.array([[[1,2],[3,4], [5,6], [7,8]]])
print(tensor)

#Hay varios métodos

#método array
array_arange = np.arange(10)

#para que me pase la matrix identidad
eye_matrix= np.eye(6)
print(eye_matrix)

#Para la matrix diagonal
diag = np.diag([1,2,3])
print(diag)

#random
random =np.random.random((2,3))
print(random)


