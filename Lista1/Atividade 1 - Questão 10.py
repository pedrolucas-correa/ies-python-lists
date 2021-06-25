print("Teste de formatação de strings")
myInteger = 12345
myFloat = 3.14159
myString = "Curso de Python"

print("Integer:", myInteger)
print("Decimal %d e um integer %d" % (myInteger, myInteger))
print("Integer Hexadecimal %x" % myInteger)
print("Float", myFloat)
print("Default %f" % myFloat)
print("Exponencial %e" % myFloat)
print("Justificar direita (%10d)" % myFloat)
print("Justificar esquerda (%-10d)" % myFloat)
print("Formar 9 digitos %.9d" % myInteger)
print("3 digitos depois do decimal (float) %.3f" % myFloat)
print("Dez e cinco caracteres permitidos na string:")
print("(%.10s)(%.5s)" % (myString, myString))
