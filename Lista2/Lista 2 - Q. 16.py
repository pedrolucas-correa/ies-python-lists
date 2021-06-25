a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor: "))

if (b - c < a) and (a < b + c):
    if a == b and b == c:
        print("Triângulo equilatero")
    elif a == b or b == c:
        print("Triângulo isosceles")
    elif a != b and b != c:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")
