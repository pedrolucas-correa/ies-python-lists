preco = float(input("Digite o valor do produto: "))
quant = int(input("Digite a quantidade de produtos: "))
print("--------------------------------------")
print("Selecione a forma de pagamento: ")
print("1 - À vista em dinheiro ou cheque")
print("2 - À vista no cartão de crédito")
print("3 - Pagamento em 2x sem juros")
print("4 - Pagamento acima de 2x")
payment = int(input())
print("--------------------------------------")

if payment == 1:
    desconto = preco * quant * 0.90
    print("R$", round(desconto, 2))
elif payment == 2:
    desconto = preco * quant * 0.85
    print("R$", round(desconto, 2))
elif payment == 3:
    valortotal = preco * quant
    print("R$", round(valortotal, 2))
else:
    juros = preco * quant * 1.10
    print("R$", round(juros, 2))
