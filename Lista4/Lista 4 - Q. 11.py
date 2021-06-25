def ip():
    endereco = input("Digite o IP: ")
    x = endereco.split(".")
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    d = int(x[3])
    if (a >= 0) and (a <= 255) and (a != 192):
        if (b >= 0) and (b <= 255) and (b != 168):
            if (c >= 0) and (c <= 255):
                if (d >= 0) and (d <= 255):
                    print("IP Válido")
    else:
        print('IP Inválido')


ip()
