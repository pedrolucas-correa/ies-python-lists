def soma():
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    limite = int(input('Define o limite: '))

    c = a + b
    if c > limite:
        print(bool(c))


def main():
    soma()


if __name__ == '__main__':
    main()
