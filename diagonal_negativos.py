n = int(input("Qual a ordem da matriz? "))
matriz = []
soma = 0

for i in range(n):
  linha = []
  for j in range(n):
    linha.append(int(input(f"Elemento [{i},{j}]: ")))
  matriz.append(linha)

print("DIAGONAL PRINCIPAL: ")
for i in range(n):
  print(matriz[i][i], end=" ")

for i in range(n):
  for j in range(n):
    if matriz[i][j] < 0:
      soma += 1

print()
print("QUANTIDADE DE NEGATIVOS = ", soma, end=" ")