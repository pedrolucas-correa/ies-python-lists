num = 1

while num != 0:
    print('--' * 30)
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))

    print(f'{x}^{y} = {x ** y}')
    print('--' * 30)
    num = int(input("Deseja continuar? "))
