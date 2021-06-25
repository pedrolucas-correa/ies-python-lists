list = []


def num():
    ns = int(input('Quantos números deseja digitar? '))
    for c in range(ns):
        numeros = int(input('Digite o número: '))
        if numeros in list:
            print('')
            print('True')
            print('')
        list.append(numeros)


num()
