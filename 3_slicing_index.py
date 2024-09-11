print("La indexación y slicing, permiten trabajar subconjuntos para evitar trabajar sobre la totalidad de datos")
import numpy as np
array= np.array([10, 20, 30, 40, 50])
print(array[2])
print("el segundo elemento")
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

print("para que me muestre extraiga los elementos por medio de cierto indice")
index = [2,0,4]
print(array[index])

print("podmeos crear matrices con números aleatorios")
array = np.random.randint(1,10, size=(3,3))
print(array)
array_exe=np.random.randint(1,200, size=(5,5))
print("ejemplo de matrix grande")
print(array_exe)
print("la posición (0,1)")
print(array_exe[0,1])
print("queremos un subarray de las dos primeras filas")
print(array_exe[:2,:2])

print("podemos imprimir una posición especifica")
print(array[0,1])

array_emunah =np.array(["HaShem", "Nachman", "Breslev", "Shejina"])
print(array_emunah)
indexe =[1,0,2]
print(array_emunah[indexe])
print("hasta el momento hemos extraído un elemento, pero se pueden sacar cortes más largos")
print(array[:2,:2])

print("ejemplos")
print("crear una matriz de 3x3")

matrix =np.array([[1,2,3],[1,28, 15],[77,16, 32]])
print(matrix)
print("la dimensión de la matriz es")
print(matrix.ndim)
print("su  forma")
print(matrix.shape)
print("tipo de dato")
print(matrix.dtype)



