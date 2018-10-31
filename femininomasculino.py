sexo = []
feminino = 0
masculino = 0 

print("Informe o sexo de tres pessoas: ")
for i in range (3):
    sexo.append(str(input()))

for sex in sexo:
  if sex == 'f':
    feminino += 1
  elif sex == 'm':
    masculino += 1
  else:    
    print('opcao invalida')

print("O número de pessoas do sexo feminino é: ", feminino, "e do sexo masculino é: ", masculino)
