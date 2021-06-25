
num = int(input("Digite o valor de n: "))

soma = 0

for divisor in range(1, num):
    if num % divisor == 0:
        soma += divisor

if num == soma:
    print(f'O numero {num} é perfeito')
else:
    print(f'O numero {num} nao é perfeito')
