from _datetime import datetime

d1 = input('Digite o dia da primeira data: ')
m1 = input('Digite o mês da primeira data: ')
y1 = input('Digite o ano da primeira data: ')
d2 = input('Digite o dia da segunda data: ')
m2 = input('Digite o mês da segunda data: ')
y2 = input("Digite o ano da segunda data: ")

data1 = datetime.strptime(f'{y1}-{m1}-{d1}', '%Y-%m-%d')
data2 = datetime.strptime(f'{y2}-{m2}-{d2}', '%Y-%m-%d')

dias = abs((data2 - data1).days)

print(dias, "dias")
