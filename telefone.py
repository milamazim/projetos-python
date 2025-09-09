nome = []
telefone = []
tipo = []
minutos = []
valorConta = []
tabelaTipos = []
minExcedente = 0

qtdClientes = int(input("Informe a quantidade de clientes: "))

for i in range(qtdClientes):
  print(f"Dados do {i+1}o. cliente:")
  nome.append(input("Nome: "))
  telefone.append(input("Telefone: "))
  tipo.append(int(input("Tipo: ")))
  minutos.append(int(input("Minutos: ")))
  print()
  
print("Informe o preco basico e excedente de cada tipo de conta:")

for i in range(3):
  linhas = []
  print(f"Tipo {i}")
  for j in range(2):
    linhas.append(float(input()))
  tabelaTipos.append(linhas)

for i in range(qtdClientes):
  if minutos[i] <= 90:  
    valorConta.append(tabelaTipos[tipo[i]][0])
  else:
    minExcedente = (minutos[i] - 90) * tabelaTipos[tipo[i]][1]
    valorConta.append(tabelaTipos[tipo[i]][0] + minExcedente)
    
print("\nRELATÓRIO DE CLIENTES:")

for i in range(qtdClientes):
  print(f"{nome[i]}, {telefone[i]}, Tipo {tipo[i]}, Minutos: {minutos[i]}, Conta = R$ {valorConta[i]:.2f}")
  