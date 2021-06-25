def maior():
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    limite = int(input('Define o limite: '))

    if (a > limite) and (b > limite):
        print('2 números maiores que o limite.')
    elif (a > limite) or (b > limite):
        print('1 número maior que o limite.')
    else:
        print('0 números maiores que o limite')


maior()
