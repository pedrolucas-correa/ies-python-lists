emprestimo = float(input("Digite o valor do empréstimo: "))

salbruto = float(input("Informe o salário bruto: "))
valprest = float(input("Insira o valor da prestação: "))

emprestimook = salbruto * 30/100

if valprest > emprestimook:
    print("----------------------------------")
    print("Empréstimo não pode ser efetuado")
else:
    print("----------------------------------")
    print("Empréstimo pode ser concedido")