num = 1
maior = ''
menor = ''

while num != 0:
    valor = float(input("Insira um valor aleatório: "))

    if maior == '':
        maior = valor
    elif menor == '':
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor

    num = int(input("Deseja continuar? "))

print("Maior número:", maior)
print("Menor número:", menor)
