tipoCha = int(input())
resposta = [int(x) for x in input().split()] # converte em int os numeros recebidos como uma lista
count = 0

for i in range(len(resposta)):  
  if (resposta[i] == tipoCha):
    count += 1

print(count)