turma = int(input("Digite a quantidade de alunos na sala: "))
provas = int(input("Digite a quantidade de provas aplicadas: "))

nota = []
mf = []
alunos = {}
media_geral = []

for a in range(0, turma):
    nota.clear()
    nome = input("Digite o nome do aluno: ")
    for c in range(0, provas):
        nota.append(float(input("Digite a nota da prova: ")))
    media = sum(nota) / provas
    media_geral.append(media)
    mf.append(sum(nota) / provas)
    alunos[media] = nome
    print(f'O aluno {nome} teve uma média de {round(sum(nota) / provas, 2)}')
    print('')

dados = alunos.get(max(mf))
if dados is not None:
    print('--' * 30)
    print(f'O aluno com maior média foi {dados} com a média {max(mf)}')

dados2 = alunos.get(min(mf))
if dados2 is not None:
    print('--' * 30)
    print(f'O aluno com menor média foi {dados2} com a média {min(mf)}')

print('')
print(f'Média geral: {round(sum(media_geral) / turma)}')
