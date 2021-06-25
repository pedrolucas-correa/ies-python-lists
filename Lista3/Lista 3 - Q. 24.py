prim = int(input("Digite um número: "))
c = 0

for n in range(1, prim + 1):
    if prim % n == 0:
        c += 1
    else:
        continue

if c == 2:
    print("{} é primo.".format(prim))
else:
    print("{} não é primo.".format(prim))
