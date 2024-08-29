import numpy as np
print("por ejemplo una empresa quiere recopliar opiniones sobre un nuevo producto ")
print("de ahí se puede sacar insgiths")
print("se quiere sacar elementos únicos y sacar su frecuencia")

survey_responses = np.array(["bueno", "excelente", "malo",
                             "bueno", "malo", "excelente",
                             "bueno", "bueno", "malo",
                             "excelente", "bueno", "malo", "malo"])

print("queremos ver los elementos que son únicos")
print(np.unique(survey_responses))

print("pero queremos saber cuales son los elementos únicos y contarlos")
unique_elements, counts =np.unique(survey_responses, return_counts=True)
print(unique_elements)
print(counts)

print("respecto a performance, hay que saber cuales elementos generan copias y cuales vistas")

array_x = np.arange(10)
view_y= array_x[1:3]
print(array_x)
print(view_y)
print("ahí cambiamos el valor de las posiciones 1 y3")
print("Ahi el que opera sobre la raíz sufre un cambio")
array_x[1:3] =[10, 11]
print(array_x)
print(view_y)

print("vamos a trabajar con copias")

array_x = np.arange(10)
copy_x =array_x[[1,2]]
print(copy_x)
array_x[1:3]=[10,11]
print(copy_x)

print("los arrays son muy manipulables")