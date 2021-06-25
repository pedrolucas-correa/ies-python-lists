
while True:

    n = float(input("Digite um número real positivo: "))

    if n > 0:
        print('--' * 20)
        print("Número válido")
        print('--' * 20)
    else:
        print('--' * 20)
        print("Número inválido, tente novamente.")
        print('--'*20)
