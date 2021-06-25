numeros = []


def ordem():
    limite = int(input('Defina o limite: '))
    c = 1

    while c > 0:
        no = int(input('Digite os números: '))
        numeros.append(no)
        numeros.sort()
        c = int(input('Deseja continuar? '))
        if c == 0:
            for x in numeros:
                if x > limite:
                    print(numeros.index(x))
                else:
                    print('-1')


ordem()
