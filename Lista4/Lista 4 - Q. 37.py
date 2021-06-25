def entrada(frase):
    palavras = frase.split()
    junto = ''.join(palavras)
    palindromo(junto)


def palindromo(junto):
    inverso = ''
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]

    if inverso == junto:
        print('Temos um palindromo!')
    else:
        print('A frase digitada nao eh um palindromo')


def main():
    frase = str(input('Digite uma frase: ')).strip().upper()
    entrada(frase)


if __name__ == "__main__":
    main()
