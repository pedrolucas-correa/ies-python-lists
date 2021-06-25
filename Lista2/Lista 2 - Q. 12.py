# 12 - Peso, Altura e IMC

#Peso e altura do usuario
peso = float(input("Digite o seu peso:"))
altura = float(input("Digite sua altura:"))

#Calculo do IMC
imc = round(peso/(altura*altura), 2)

#Imprimir IMC
print("IMC:", imc, "Kg/m²")
print("---------------------------")

#IMC Classificação
if (imc < 18,5):
    print("Abaixo do peso")
elif (imc >= 18,5) and (imc < 25):
    print ("Normal")
elif (imc >= 25) and (imc < 30):
    print ("Acima do peso")
else:
    print("Obeso")