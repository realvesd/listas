prod = []
inferior = 0
medio = 0
acima = 0

print("Informe o preço do produto: ")

for i in range (5):
  prod.append(float(input()))

for preco in prod:
  if preco <= 50.00:
    inferior += 1
  elif preco > 50.00 and preco <= 80.00:
    medio += 1
  elif preco > 80.00:
    acima += 1
  
  media = sum(prod)/5

print("A quantidade de produtos de valor inferior a R$ 50.00 foi: ", inferior, "produtos entre R$ 50.00 e R$ 80.00 foi: ", medio, "e de valor superior a R$ 50.00 foi: ", superior. ". A média de preço dos produtos é: ", media)
