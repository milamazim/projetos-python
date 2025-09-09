'''
Fazer um programa para ler uma quantidade N (supor N > 0), depois ler os dados de N atletas (nome,
sexo, altura, peso). Depois, mostrar um relatório contendo:
 Peso médio dos atletas
 Nome do atleta mais alto
 Porcentagem de homens
 Altura média das mulheres
Caso não sejam digitadas mulheres, a altura média não poderá ser calculada (pois divisão por zero não
existe). Neste caso, apenas mostrar a mensagem "Não há mulheres cadastradas".
Fazer validações de dados para altura e peso, não permitindo digitar valores não positivos para esses
dados. Faça também a validação do sexo, não permitindo valores diferentes de F e M.
Dica: para validar o sexo, a lógica é: tem que pedir para o usuário digitar novamente enquanto o valor
digitado for diferente de "F" E diferente de "M"
'''

qtdAtletas = int(input("Qual a quantidade de atletas? "))

maiorAltura = 0
atletasM = 0
atletasF = 0
alturaTotalMulheres = 0
pesoTotalAtletas = 0

for atleta in range(1, qtdAtletas+1):
  print(f"Digite os dados do atleta numero {atleta}")
  nomeAtleta = input("Nome: ")
  sexoAtleta = input("Sexo: ")
  
  while((sexoAtleta != 'F') and (sexoAtleta != 'M')):
    sexoAtleta = input("Valor invalido! Favor digitar F ou M: ") 
   
  alturaAtleta = float(input("Altura: "))
  
  while(alturaAtleta <= 0):
    alturaAtleta = float(input("Valor invalido! Favor digitar um valor positivo: "))
  
  if alturaAtleta > maiorAltura:
    maiorAltura = alturaAtleta
    atletaMaisAlto = nomeAtleta
   
  if (sexoAtleta == 'M'):
    atletasM += 1
  else:
    atletasF += 1
    alturaTotalMulheres += alturaAtleta
    
  pesoAtleta = float(input("Peso: "))
  
  while(pesoAtleta <= 0):
    pesoAtleta = float(input("Valor invalido! Favor digitar um valor positivo: "))
    
  pesoTotalAtletas += pesoAtleta

pesoMedioAtletas = pesoTotalAtletas / qtdAtletas
porcentagemHomens = atletasM / qtdAtletas * 100
   
print("\nRELATÓRIO:")
print(f"Peso médio dos atletas: {pesoMedioAtletas:.2f}")
print(f"Atleta mais alto: {atletaMaisAlto}")
print(f"Porcentagem de homens: {porcentagemHomens:.1f}%")

if atletasF > 0:
  alturaMediaMulheres = alturaTotalMulheres / atletasF
  print(f"Altura média das mulheres: {alturaMediaMulheres:.2f}")
else:
  print("Não há mulheres cadastradas")  