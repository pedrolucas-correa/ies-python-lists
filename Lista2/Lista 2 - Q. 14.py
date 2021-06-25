matricula = int(input("Digite o número de matricula: "))
n1 = float(input("Digite sua 1º nota: "))
n2 = float(input("Digite sua 2º nota: "))
n3 = float(input("Digite sua 3º nota: "))
me = (n1 + n2 + n3) / 3

ma = (n1 + (n2 * 2) + (n3 * 3) + me) / 7

print("Aluno:", matricula, ", Média de aproveitamento:", round(ma, 2))
