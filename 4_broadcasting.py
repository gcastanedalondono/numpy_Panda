import numpy as np

print("numpy trta los arrays y sus operaciones alargandles la longitud de forma implicita")
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





