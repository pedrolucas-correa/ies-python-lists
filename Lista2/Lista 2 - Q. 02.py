nome = input("Digite seu nome: ")
sexo = int(input("Digite seu sexo, 1 para genero feminino ou 2 para masculino: "))
estadocivil = int(input("Digite seu estado civil, 1 p/ solteiro, 2 p/ casado, 3 p/ divorciado ou 4 p/ viúvo: "))

if (sexo == 1) and (estadocivil == 2):
    tempoc = input("Há quanto tempo está casada? ")
    print("Cadastro conlcuido Sra.", nome)
else:
    print("Cadastro concluido", nome)
