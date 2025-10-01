def impostoSobreSalario(quantia):
  if (quantia/12 < 3000):
    return 0
  elif (quantia/12 < 5000):
    return quantia * 0.10
  else:
    return quantia * 0.2    
  
def impostoSobreServicos(quantia):  
  return quantia * 0.15

def impostoSobreGC(quantia):
  return quantia * 0.2

def impostoBrutoTotal(salario, servicos, gc):
  return impostoSobreSalario(salario) + impostoSobreServicos(servicos) + impostoSobreGC(gc)

def abatimento(salario, servicos, gc, gastosMedicos, gastosEducacionais):
  maxAbatimento = impostoBrutoTotal(salario, servicos, gc) * 0.3
  somaGastos = gastosMedicos + gastosEducacionais
  
  if (somaGastos < maxAbatimento):
    return somaGastos
  else:
    return maxAbatimento

def impostoDevido(salario, servicos, gc, gastosMedicos, gastosEducacionais):  
  return impostoBrutoTotal(salario, servicos, gc) - abatimento(salario, servicos, gc, gastosMedicos, gastosEducacionais)

print("Digite os dados do contribuinte: ")

rendaAnualSalarios = float(input("Renda anual com salário: "))
rendaAnualPrestacaoServicos = float(input("Renda anual com prestação de serviço: "))
rendaAnualGanhoCapital = float(input("Renda anual com ganho de capital: "))
gastosMedicos = float(input("Gastos médicos: "))
gastosEducacionais = float(input("Gastos médicos: "))

print()
print("Relatório: ")
print(f"Imposto sobre salário: {impostoSobreSalario(rendaAnualSalarios):.2f}")
print(f"Imposto sobre serviços: {impostoSobreServicos(rendaAnualPrestacaoServicos):.2f}")
print(f"Imposto sobre ganho de capital: {impostoSobreGC(rendaAnualGanhoCapital):.2f}")
print(f"Imposto bruto total: {impostoBrutoTotal(rendaAnualSalarios, rendaAnualPrestacaoServicos, rendaAnualGanhoCapital):.2f}")
print(f"Abatimento: {abatimento(rendaAnualSalarios, rendaAnualPrestacaoServicos, rendaAnualGanhoCapital, gastosMedicos, gastosEducacionais):.2f}")
print(f"Imposto devido: {impostoDevido(rendaAnualSalarios, rendaAnualPrestacaoServicos, rendaAnualGanhoCapital, gastosMedicos, gastosEducacionais):.2f}")