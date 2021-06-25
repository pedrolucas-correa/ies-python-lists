turma = int(input("Digite a quantidade de alunos na sala: "))
provas = int(input("Digite a quantidade de provas aplicadas: "))

nota = []
mf = []
alunos = {}

for a in range(0, turma):
    nota.clear()
    nome = input("Digite o nome do aluno: ")
    for c in range(0, provas):
        nota.append(float(input("Digite a nota da prova: ")))
    media = sum(nota) / provas
    mf.append(sum(nota) / provas)
    alunos[media] = nome
    print(f'O aluno {nome} teve uma média de {sum(nota) / provas}')
    print('')

dados = alunos.get(max(mf))
if dados is not None:
    print('--' * 30)
    print(f'O aluno com maior média foi {dados} com média: {max(mf)}')
