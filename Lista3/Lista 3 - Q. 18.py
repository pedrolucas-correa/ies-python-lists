result = 1

while result != 0:
    x = int(input("Digite um valor: "))
    y = int(input("Digite um valor: "))
    op = int(input("| 1 - soma | 2 - produto | 3 - divisão | 4 - potência | "))

    if op == 1:
        result = x + y
        print(result)
    elif op == 2:
        result = x * y
        print(result)
    elif op == 3:
        result = x / y
        print(result)
    else:
        result = x ** y
        print(result)
