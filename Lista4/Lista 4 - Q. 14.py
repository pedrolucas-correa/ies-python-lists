def conceito():
    nota = float(input('Digite a nota do aluno: '))

    if nota >= 8.5:
        print('Nota conceito A')
    elif (nota < 8.5) and (nota >= 7):
        print('Nota conceito B')
    elif (nota < 7) and (nota >= 5):
        print('Nota conceito C')
    elif (nota < 5) and (nota >= 3):
        print('Nota conceito D')
    elif (nota < 3) and (nota >= 1):
        print('Nota conceito E')
    else:
        print('Nota conceito F')


conceito()
