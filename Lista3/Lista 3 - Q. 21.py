def num(x1, x2, x3):
    soma = x1 + x2 + x3
    prod = x1 * x2 * x3
    media = (x1 + x2 + x3) / 3
    print("Soma:", round(soma, 2))
    print("Produto:", round(prod, 2))
    print("Media:", round(media, 2))
    return round(soma, 2), round(prod, 2), round(media, 2)


conj = int(input("Quantos conjuntos? "))

for c in range(0, conj):
    x1 = float(input("Digite um número: "))
    x2 = float(input("Digite um número: "))
    x3 = float(input("Digite um número: "))

    if x1 < x2 < x3:
        print('--' * 20)
        print(num(x1, x2, x3))
        print('--' * 20)
        continue
    else:
        print('--' * 30)
        print("Entre com os números em ordem crescente! ")
        print('--' * 30)
        break
