bfem = []
bmale = []
female = '0 Mulheres candidatas'
qntfem = 0
maior = 0
m = 0
male = 0
a = 0
menor = 0
media = []
mf = 0
porc = 0

while a >= 0:
    a = int(input('Digite o número de inscrição: '))
    if a == -1:
        print('--' * 45)
        print('Programa finalizado')
        print('--' * 45)
        continue
    c = input('Digite seu sexo (M/F): ')
    c = c.upper()
    if c == 'F':
        female += 1  # Quantidade de mulheres candidatas
        bf = (int(input('Digite sua idade: ')))
        bfem.append(bf)
        d = input('Possui experiencia anterior (S/N): ').upper()
        d = d.upper()
        if d == 'S':  # Mulher com experiencia anterior que possui a menor idade
            menor = min(bfem)
            if bf < 35:  # Quantidade de mulheres menores que 35 anos de idade e com experiencia anterior
                qntfem += 1
    elif c == 'M':
        male += 1
        bm = (int(input('Digite sua idade: ')))
        bmale.append(bm)
        d = input('Possui experiencia anterior (S/N): ')
        d = d.upper()
        if bm > 45:  # Porcentagem de homens maiores que 45 anos de idade
            maior += 1
            porc = maior / male * 100
        if d == 'S':  # Media da idade dos homens com experiencia anterior
            m += 1
            media.append(bm)
            mf = sum(media) / m

print(f'Quantidade de mulheres candidatas: {female}')
print(f'Idade média dos homens com experiência anterior: {float(round(mf, 2))}')
print(f'Porcentagem dos homens com mais de 45 anos: {float(round(porc, 2))}%')
print(f'Quantidade de mulheres com idade inferior a 35 anos e com experiencia anterior: {qntfem}')
print(f'Mulher com menor idade entre as que possuem experiência anterior: {menor}')
print('--' * 45)
