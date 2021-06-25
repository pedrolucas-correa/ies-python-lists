def num():
    n = int(input('Digite um valor: '))
    if n >= 0:
        print(f'O número {n} é positivo')
    else:
        print(f'O número {n} é negativo')


def main():
    num()


if __name__ == '__main__':
    main()
