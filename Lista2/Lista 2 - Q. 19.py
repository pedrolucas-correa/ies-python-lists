a = int(input("Insira o valor de A: "))
b = int(input("Insira o valor de B: "))
c = int(input("Insira o valor de C: "))

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print("Não existe raizes reais")
else:
    x1 = (-b + (delta ** 0.5)) / 2 * a
    x2 = (-b - (delta ** 0.5)) / 2 * a
    print("x' =", x1)
    print("x'' =", x2)
