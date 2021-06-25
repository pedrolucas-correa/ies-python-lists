n = 0
somapar = []
somaimpar = []

while n <= 1000:
    n = int(input("Digite números positivos inteiros: "))
    print('--' * 20)

    if n > 1000:
        break
    if n % 2 == 0:
        somapar.append(n)
    if n % 2 != 0:
        somaimpar.append(n)

print("Soma dos números pares:", sum(somapar))
print("Soma dos números impares:", sum(somaimpar))
print('--' * 21)
