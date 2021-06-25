vendas = []

func = 1

while func > 0:
    venda = float(input('Digite o total de venda mensal: '))
    vendas.append(venda)
    if venda > 3000:
        sal = venda * 0.65
        print('Comissão do corretor: ', sal)
    elif (venda >= 1500) and (venda <= 3000):
        sal = venda * 0.80
        print('Comissão do corretor: ', sal)
    else:
        sal = venda * 0.87
        print('Comissão do corretor: ', sal)
    print('')
    func = int(input('Deseja continuar? (1 - Sim | 0 - Não) '))
    print('')

    if func == 0:
        print('Total de vendas da companhia: ', sum(vendas))
