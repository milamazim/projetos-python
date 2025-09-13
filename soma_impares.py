print("Digite dois números: ")
x = int(input())
y = int(input())

if (x > y):
  maior = x
  menor = y
else:
  maior = y
  menor = x

soma = 0

for numero in range (menor+1, maior):
  if (numero % 2 != 0):    
    soma += numero

print("SOMA DOS ÍMPARES = ", soma)