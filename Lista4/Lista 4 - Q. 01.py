def valor():
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    numeros = 0
    if x == y:
        print(f"Valores iguais ({x}|{y})")
    elif x < y:
        print("Menor valor:", x)
        numeros = x
    else:
        print("Menor valor:", y)
        numeros = y
    return numeros


def main():
    valor()


if __name__ == '__main__':
    main()
