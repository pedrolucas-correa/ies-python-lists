number = int(input("Digite um número de 1 a 7: "))

"""De acordo com a Organização Internacional de Padronização (ISO), 1º dia da semana é a Segunda-feira"""

if number == 1:
    print("Segunda-feira")
elif number == 2:
    print("Terça-feira")
elif number == 3:
    print("Quarta-feira")
elif number == 4:
    print("Quinta-feira")
elif number == 5:
    print("Sexta-feira")
elif number == 6:
    print("Sábado")
elif number == 7:
    print("Domingo")
else:
    print("Número inválido : não existe dia da semana com esse número")
