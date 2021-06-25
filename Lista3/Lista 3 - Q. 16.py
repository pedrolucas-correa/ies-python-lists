massa = float(input("Digite a massa em gramas: "))
t = 0
print("Massa inicial (g):", massa)
while massa > 0.5:
    massa = massa / 2
    t += 50

print("Massa final (g):", round(massa, 3))
print("Tempo decorrido em minutos:", round(t / 60, 2))
