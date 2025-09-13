n = int(input("Quantos números você vai digitar? "))
valores = []
soma = 0

for i in range(n):
  valores.append(float(input("Digite um número: ")))
  soma += valores[i]

print()
print("VALORES = ", end=' ')
for i in range(n):
  print(f"{valores[i]:.1f}", end=' ')

media = soma / n

print()
print(f"SOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")