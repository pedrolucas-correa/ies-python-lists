try:
    nome = input("Digite seu nome: ")

    dias = int(input("Digite o número de dias que irá se hospedar: "))
    if dias > 0:
        if dias < 15:
            valor = dias * 300 + 20
            print("Nome:", nome, ",", "Total a pagar:", valor)
        elif dias == 15:
            valor = dias * 300 + 14
            print("Nome:", nome, ",", "Total a pagar:", valor)
        else:
            valor = dias * 300 + 12
            print("Nome:", nome, ",", "Total a pagar:", valor)
    else:
        print("Insira um valor diferente ou maior que 0")
except:
    print("Insira os valores corretamente")
