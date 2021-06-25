n = int(input("Digite o valor de n: "))
print("São números primos: ")
for i in range(2, n):
    j = 2
    c = 0

    while j < i:
        if i % j == 0:
            c = 1
            j += 1
        else:
            j += 1

    if c == 0:
        print(i)
    else:
        c = 0
