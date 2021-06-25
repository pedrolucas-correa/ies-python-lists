matricula = int(input("Digite o número de matricula: "))
n1 = float(input("Digite sua 1º nota: "))
n2 = float(input("Digite sua 2º nota: "))
n3 = float(input("Digite sua 3º nota: "))
me = (n1 + n2 + n3) / 3

ma = (n1 + (n2 * 2) + (n3 * 3) + me) / 7
print("Aluno:", matricula)
print("Notas:", n1, ",", n2, ",", n3)
print("Média dos exercicios:", round(me, 2))
print("Média de aproveitamento:", round(ma, 2))

if ma >= 90:
    conceito = "A"
    print("Conceito da média de aproveitamento:", conceito)
    print("APROVADO")
elif (ma >= 75) and (ma < 90):
    conceito = "B"
    print("Conceito da média de aproveitamento:", conceito)
    print("APROVADO")
elif (ma >= 60) and (ma < 75):
    conceito = "C"
    print("Conceito da média de aproveitamento:", conceito)
    print("APROVADO")
elif (ma >= 40) and (ma < 60):
    conceito = "D"
    print("Conceito da média de aproveitamento:", conceito)
    print("REPROVADO")
else:
    conceito = "E"
    print("Conceito da média de aproveitamento:", conceito)
    print("REPROVADO")
