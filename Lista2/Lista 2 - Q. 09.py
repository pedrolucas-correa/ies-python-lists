a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
c = int(input("Digite o valor de C"))
d = int(input("Digite o valor de D"))

maior = a

if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d

print("Maior: ", maior)

menor = a

if b < menor:
    menor = b
if c < menor:
    menor = c
if d < menor:
    menor = d

print("Menor: ", menor)
