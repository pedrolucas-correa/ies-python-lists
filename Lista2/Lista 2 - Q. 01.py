try:
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    ab = a + b

    if ab < c:
        print("A soma de A + B é menor que C")
    else:
        print("A soma de A + B é maior que C")
except:
    print("Insira os valores corretamente")
