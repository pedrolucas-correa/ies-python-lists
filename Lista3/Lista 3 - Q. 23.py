n = int(input("Digite o valor de n: "))
c = 0
i = 0

for c in range(c, n * 2):
    c += 1
    if c < n * 2:
        if c % 2 == 1:
            print("Impar:", c)

print('--' * 30)

for i in range(i, n * 2):
    i += 1
    if i < ((n * 2) + 1):
        if i % 2 == 0:
            print("Par:", i)
