quest = []
otimo = 0
bom = 0
regular = 0

print("Informe sua opiniao em relacao ao filme assistido, 3 para otimo, 2 para bom e 1 para regular: ")

for i in range (5):
  quest.append(str(input()))

for resposta in quest:
  if resposta == '3':
    otimo += 1
  elif resposta == '2':
    bom += 1
  elif resposta == '1':
    regular += 1
  else:
    print('Opção invalida!')

print("A quantidade de pessoas que achou o filme otimo foi: ", otimo, 'que achou o filme bom: ',bom, 'e que achou o filme regular: ', regular)
