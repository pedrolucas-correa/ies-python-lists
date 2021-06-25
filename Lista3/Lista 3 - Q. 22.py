maior = 0
menor = 0
medias = []

aln = int(input("Média de quantos alunos serão inseridas?"))

for c in range(0, aln):
    media = float(input("Insira a média do aluno: "))
    medias.append(media)

    if media < 0:
        print("Média negativa")
        break
    elif maior == 0:
        maior = media
    elif menor == 0:
        menor = media
    else:
        if media > maior:
            maior = media
        elif media < menor:
            menor = media

print("Maior média:", maior)
print("Menor média:", menor)
print("Média dos alunos:", round(sum(medias) / aln, 2))
