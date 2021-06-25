def convert():
    f = float(input('Digite uma temperatura em Fahrenheit: '))
    celsius = (f - 32) * 5 / 9
    print(f'A temperatura em Cº é: {celsius}')


convert()
