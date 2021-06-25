a = 0
b = 1
limite = int(input(" Entre com o limite da série de fibonacci: "))

while b < limite:
    print(b)
    a, b = b, a + b
