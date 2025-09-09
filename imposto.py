'''
Para calcular o imposto de renda que uma pessoa deve pagar, um país aplica as seguintes regras:
1) Imposto sobre salário: a pessoa paga imposto sobre seu salário conforme
tabela ao lado

Salário MENSAL                Imposto
Abaixo de 3000 por mês        Isento
3000 até 5000 exclusive       10%
5000 ou acima                 20%

2) Se a pessoa obteve renda com prestação de serviços, o imposto cobrado é de 15%.

3) Se a pessoa obteve ganho de capital (imóveis, ações, etc.), o imposto cobrado é de 20%.

4) A pessoa pode abater até 30% do seu imposto bruto devido com gastos médicos ou educacionais. Mas
se seus gastos médicos e educacionais forem abaixo desses 30%, apenas os gastos médicos e
educacionais podem ser abatidos.

Fazer um programa para ler quanto a pessoa obteve de renda anual com salário, prestação de serviço e
ganho de capital. Leia também quando a pessoal teve de gastos médicos e educacionais no ano. Seu
programa deverá então produzir um relatório de imposto de renda dessa pessoa conforme exemplos.
Considere a renda mensal com salário como sendo a renda anual dividida por 12.
'''

rendaAnualSalarios = float(input("Renda anual com salário: "))
rendaAnualPrestacaoServicos = float(input("Renda anual com prestação de serviço: "))
rendaAnualGanhoCapital = float(input("Renda anual com ganho de capital: "))
gastosMedicos = float(input("Gastos médicos: "))
gastosEducacionais = float(input("Gastos educacionais: "))
impostoServicos = 0
impostoGanhoCapital = 0

if (rendaAnualSalarios / 12) < 3000:
  impostoSalario = 0
elif (rendaAnualSalarios / 12) < 5000:
  impostoSalario = rendaAnualSalarios * 0.1
else:
  impostoSalario = rendaAnualSalarios * 0.2

if rendaAnualPrestacaoServicos > 0:
  impostoServicos = rendaAnualPrestacaoServicos * 0.15 

if rendaAnualGanhoCapital > 0:
  impostoGanhoCapital = rendaAnualGanhoCapital * 0.2

impostoBrutoTotal = impostoSalario + impostoServicos + impostoGanhoCapital
gastosDedutiveis = gastosMedicos + gastosEducacionais
maximoDedutivel = impostoBrutoTotal * 0.3

if gastosDedutiveis > maximoDedutivel:
  abatimento = maximoDedutivel
else:
  abatimento = gastosDedutiveis

impostoDevido = impostoBrutoTotal - abatimento

print("\nRELATÓRIO DE IMPOSTO DE RENDA")
print("\nCONSOLIDADO DE RENDA: ")
print(f"Imposto sobre salário: {impostoSalario:.2f}")
print(f"Imposto sobre serviços: {impostoServicos:.2f}")
print(f"Imposto sobre ganho de capital: {impostoGanhoCapital:.2f}")
print("\nDEDUÇÕES:")
print(f"Máximo dedutível: {maximoDedutivel:.2f}")
print(f"Gastos dedutíveis: {gastosDedutiveis:.2f}")
print("\nRESUMO:")
print(f"Imposto bruto total: {impostoBrutoTotal:.2f}")
print(f"Abatimento: {abatimento:.2f}")
print(f"Imposto devido: {impostoDevido:.2f}")