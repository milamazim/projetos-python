'''
Em um bar, o ingresso custa 10 reais para homens e 8 reais para mulheres. Cada cerveja custa 5
reais, cada refrigerante 3 reais e cada espetinho custa 7. Além disso, o bar cobra uma taxa de
couvert artístico no valor de 4 reais, porém, se o valor gasto com consumo for superior a 30 reais,
o couvert artístico não é cobrado. Fazer um programa para ler os seguintes dados de um cliente do
bar: sexo (F ou M), quantidade de cervejas, refrigerantes e espetinhos consumidos. O programa
deve então mostrar um relatório com a conta a ser paga pelo cliente.
'''
ingressoM = 10
ingressoF = 8
precoCerveja = 5
precoRefri = 3
precoEspetinho = 7
taxaCouvert = 4

sexo = input("Sexo: ")
qtdCerveja = int(input("Quantidade de cervejas: "))
qtdRefri = int(input("Quantidade de refrigerantes: "))
qtdEspetinho = int(input("Quantidade de espetinhos: "))

valorConsumo = (precoCerveja * qtdCerveja) + (precoRefri * qtdRefri) + (precoEspetinho * qtdEspetinho)

print(f"\nRELATÓRIO: ") 
print(f"Consumo = R$ {valorConsumo:.2f}")

if valorConsumo > 30:
  valorCouvert = 0  
  print("Isento de Couvert")
else:
  valorCouvert = taxaCouvert
  print(f"Couvert = R$ {valorCouvert:.2f} \n")

if sexo == 'F':
  valorIngresso = ingressoF
else:
  valorIngresso = ingressoM

print(f"Ingresso = R$ {valorIngresso:.2f}\n")

valorTotal = valorConsumo + valorCouvert + valorIngresso

print(f"Valor a pagar = R$ {valorTotal:.2f}")