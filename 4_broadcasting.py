import numpy as np

print("numpy trata los arrays y sus operaciones alargandoles la longitud de forma implicita")
print("vamos a trabajar con una lista de precios de una tienda")

prices =np.array([100, 200, 300])
discount =np.array([0.9])
discount_prices = prices*discount
print(discount_prices)

print("ejemplo generando un array de números aleatorios")
prices =np.random.randint(100, 500, size=(3,3))
discount = np.array([10, 20, 30])
discount_prices =prices + discount
print(prices)

print("precios + descuentos")
print(discount_prices)

print("un ejemplo mio")
precios =np.random.randint(0,100, size=(4,4))
descuento = np.array([10, 15, 20, 25])
print(precios)
precio_descuento= precios - descuento
print(precio_descuento)

print("dentro de los arrays también se pueden hacer operaciones lógicas")
array =np.array([1,2,3,4,5])
print("ésta la aplica a todos los elementos")
print(np.all(array > 9))

print("Esta la va a aplicar a algún elemento")
print(np.any(array > 4))
print("pero yo creía que me mostraba el elemento en cuestión")

print("también está el concepto de concatenación, para unir varios elementos")
array_a = np.array([1,2,3])
array_b = np.array([4,5,6])
concatenated =np.concatenate((array_a, array_b))
print(concatenated)

print("también contamos con el stacking,nos permite apilar arrays o darles otra especificidad ")
stacked_v=np.vstack((array_a,array_b))
print("la concatenación lo hace de manera horizontal, este(np.vstack)es de manera vertical")
print(stacked_v)

stacked_h = np.hstack((array_a, array_b))
print("este los organiza de manera horizontal el np.hstack")
print(stacked_h)

print("ahora vamos a dividir un array de tres en tres")
array_c = np.arange(1,10)
split_array = np.split(array_c, 3)
print(array)
print(split_array)







