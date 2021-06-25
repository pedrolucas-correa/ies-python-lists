maior = 0
menor = 0

for n in range(1, 16):
    valor = float(input("Insira um valor aleatório: "))

    if maior == 0:
        maior = valor
    elif menor == 0:
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor

print("Maior número:", maior)
print("Menor número:", menor)
