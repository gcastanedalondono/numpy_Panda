import numpy as np

print("numpy trta los arrays y sus operaciones alargandles la longitud de forma implicita")
print("vamos a trabajar con una lista de precios de una tienda")

prices =np.array([100, 200, 300])
discount =np.array([0.9])
discount_prices = prices*discount
print(discount_prices)
