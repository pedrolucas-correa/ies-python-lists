def convert():
    f = 30.2
    c = -1

    while c <= 100:
        f += 1.8
        c = (f - 32) * 5 / 9
        print('--' * 30)
        print(f'A temperatura Fº {round(f, 2)}º')
        print(f'A temperatura em Cº é {round(c, 2)}º')


def main():
    convert()


if __name__ == '__main__':
    main()
