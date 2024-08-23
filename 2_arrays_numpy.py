import numpy as np

print("sirven para representar sónidos, imagenes y datos cientificos")
print("se utiliza en IA")
print("un array en NumPy es una estructura de datos homogénea organizada en una o más dimensiones")
print("manejas arrays es más eficiente que manejar listas")


array =np.array([[1,2,3],[4,5,6]])
print("su dimensión")
print(array.ndim)
print("su forma")
print(array.shape)
print("tipo de dato")
print(array.dtype)
print("nos dice el tipo de elemento que tenemos, entero, flotante o booleano")
print("tenemos el uint 8, representa valores de un byte, entre 0 -255, no negativos, puede ser como los colores ")
print("float32, representa valores decimales para cálculos de precisión moderada pero necestian ahorrar memoria")
print("float64: Represeta números de punto flotante de doble precisión ,es muy utilizado den numpy")
      
print("el primer tipo de dato")      
z= np.array(3, dtype=np.uint8)
print(z)
      
print("essta volviendo los enteros decimales")      
double_array = np.array([1,2,3], dtype='d')
print(double_array)

print("vamos a hacer una conversión de tipo de dato")
z =z.astype(np.float64)
print(z)    

print("sumando los elementos del array")
sum= np.sum(array)
print(sum)

print("sacando la media")
mean =np.mean(array)
print(mean) 
 