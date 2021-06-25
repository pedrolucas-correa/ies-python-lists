soma = []


def menor():
    n = int(input('Defina N: '))

    for c in range(0, n + 1):
        soma.append(c)

    print(f'A soma dos números menores ou iguais a N é: {sum(soma)}')


menor()
