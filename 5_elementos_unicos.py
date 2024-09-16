import numpy as np
print("por ejemplo una empresa quiere recopliar opiniones sobre un nuevo producto ")
print("de ahí se puede sacar insgiths")
print("se quiere sacar elementos únicos y sacar su frecuencia")

survey_responses = np.array(["bueno", "excelente", "malo",
                             "bueno", "malo", "excelente",
                             "bueno", "bueno", "malo",
                             "excelente", "bueno", "malo", "malo", "HaShem ayudame con la ansiedad"])

Breslev = np.array(["HaShem","HaShem", "Emunah", "Najman", "Ratzon", "simja", "simja", "Torah", "HaShem", "Emunah"])

print("Para ver los elementos únicos de ambos arrays")
print(np.unique(survey_responses))
print(np.unique(Breslev))
print("queremos ver cuantas veces aparece un elemento")
unique_elements, counts=np.unique(survey_responses, return_counts=True)
print(unique_elements)
print(counts)
print("para el array de Breslev")
elementos_unicos, counts=np.unique(Breslev, return_counts=True)
print(elementos_unicos)
print(counts)

print("queremos ver que operaciones regresan copias y cuales vistas")

array_x = np.arange(10)
view_y=array_x[1:3]
print(array_x)
print(view_y)
print("modificamos los valores de un elemento del array, entonces la vista también se verá modificada")
print("Creamos copias para que no se modifique la raíz, cuando guardamos en nuevas variables")

array_x[1:3] =[10, 11]
print(array_x)
print(view_y)

copy_x =array_x[[1,2]]
print(array_x)
print(view_y)
array_x[1:3] =[22, 14]
print(array_x)
print("aquí no se realiza modificación en la raíz")
print(copy_x)
