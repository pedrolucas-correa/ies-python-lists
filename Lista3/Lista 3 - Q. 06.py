mult = 1
n = 1

while True:
    if n != 0:
        print('--' * 18)
        n = int(input("Digite um valor: "))
        mult = mult * n
        print("O produto dos números é:", mult)
    else:
        print("PROGRAMA FINALIZADO")
        break
        
