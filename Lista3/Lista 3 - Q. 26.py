par = []
n1 = int(input(" Digite o 1. valor: "))
n2 = int(input(" Digite o 2. valor: "))
mult = 1
n = n1
i = n1
for c in range(n1, n2):
    n += 1
    if n % 2 == 0:
        par.append(n)

print(" Soma dos pares:", sum(par))

for c in range(n1, n2):
    i += 1
    if i % 2 != 0:
        mult *= i

print(" Multiplicação dos ímpares:", mult)
