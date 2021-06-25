def area():
    pi = 3.14
    raio = float(input('Digite o raio do circulo: '))

    ac = pi * (raio ** 2)

    print(f'Área do circulo = {round(ac, 2)}')


area()
