numeros = []

print("Informe seis numeros inteiros: ")
for i in range(5):
  numeros.append(int(input()))

for num in numeros:
  if num >= 0:
    print(num)
