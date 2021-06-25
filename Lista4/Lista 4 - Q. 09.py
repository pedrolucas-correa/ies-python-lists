def is_anagram(palavra1, palavra2):
    cont = 0
    for c in palavra1:
        for letra in c:
            if letra in palavra2:
                cont += 1
    print("_" * 30)
    if cont == len(palavra2):
        print(f"{palavra1} e {palavra2}")
        print("Formam um anagrama")
        print(f"Resultado = {cont == len(palavra2)}")

    else:
        print(f"{palavra1} e {palavra2}")
        print("Não formam um anagrama")
        print(f"Resultado = {cont == len(palavra2)}")


palavra1 = str(input("Digite uma palavra: ")).upper()
palavra2 = str(input("Digite outra palavra: ")).upper()
is_anagram(palavra1, palavra2)
