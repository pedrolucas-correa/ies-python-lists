sexo = int(input("Digite 1 para feminino e 2 para masculino: "))
altura = float(input("Digite sua altura: "))

if sexo == 2:
    pesoideal = (72.7 * altura) - 58
    print("Seu peso ideal é: ", round(pesoideal, 2))
else:
    pesoideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é: ", round(pesoideal, 2))
