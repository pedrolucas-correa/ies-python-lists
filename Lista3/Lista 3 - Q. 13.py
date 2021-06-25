n = 1
media = []
x = 0
while n != 0:
    valor = int(input("Insira um valor aleatório: "))

    if valor % 2 == 0:
        x += 1
        media.append(valor)
        print('--' * 20)

    n = int(input("Deseja continuar? "))

    if n == 0:
        print('--' * 20)
        print("Média dos números pares:", round(sum(media) / x, 2))
        print('--' * 20)
