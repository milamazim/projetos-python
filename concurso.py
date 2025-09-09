'''
Fazer um programa para ler uma quantidade N, depois ler os dados de N pessoas que participaram de um concurso
que teve duas etapas de provas. Para cada pessoa, os dados lidos serão: nome, nota da etapa 1, e nota da etapa 2.
Você deve guardar os dados das pessoas em vetores.
A nota de cada etapa do concurso pode variar de 0 a 100 (não precisa verificar). Uma pessoa é aprovada no
concurso se obtiver a nota média de 70 pontos (média das duas etapas).
Depois de ler os dados das pessoas, seu programa deverá mostrar:
- Tabela de pessoas inclusive com suas médias
- Nomes das pessoas aprovadas (dica: veja exercícios negativos, alturas, abaixo_da_media, aprovados)
- Porcentagem de aprovação (dica: veja exercícios alturas)
- Nome da pessoa de maior média (supor não haver empates) (dica: veja exercícios maior_posicao, mais_velho)
- Nota média somente das pessoas aprovadas (dica: veja exercícios media_pares, dados_pessoas)
Se não houver candidatos aprovados, ao invés de mostrar a média, mostrar a mensagem "Não há candidatos
aprovados".
'''

nomes = []
notasEtapa1 = []
notasEtapa2 = []
medias = []
maiorMedia = 0
aprovados = 0
notasAprovados = 0

qtdPessoas = int(input("Qual a quantidade de pessoas? "))

for n in range(qtdPessoas):
  print(f"Digite os dados da {n+1}a pessoa:")
  nomes.append(input("Nome: "))
  notasEtapa1.append(float(input("Nota etapa 1: ")))
  notasEtapa2.append(float(input("Nota etapa 2: ")))
  
print("\nTABELA: ")

for n in range(qtdPessoas):
  medias.append((notasEtapa1[n] + notasEtapa2[n]) / 2)
  print(f"{nomes[n]}, {notasEtapa1[n]:.1f}, {notasEtapa2[n]:.1f}, MEDIA = {medias[n]:.2f}")

print("\nPESSOAS APROVADAS:")

for n in range(qtdPessoas):
  if (medias[n] >= 70):
    aprovados += 1
    notasAprovados += medias[n]
    print(nomes[n])
  
  if (medias[n] > maiorMedia):
    maiorMedia = medias[n]
    pessoaMaiorMedia = nomes[n]
 
percentualAprovados = aprovados / qtdPessoas * 100

print(f"\nPorcentagem de aprovação: {percentualAprovados:.1f}%")
print(f"Maior média: {pessoaMaiorMedia}")

if aprovados > 0:
  notaMediaAprovados = notasAprovados / aprovados
  print(f"Nota média dos aprovados: {notaMediaAprovados:.2f}")
else:
  print("Não há candidatos aprovados")