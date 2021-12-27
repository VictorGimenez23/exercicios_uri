valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print(f"NOTAS:")
for n in notas:
    qtdeNotas = int(valor / n)
    print(f"{qtdeNotas} nota(s) de R$ {n:.2f}")
    valor = valor - (qtdeNotas * n)
print(f"MOEDAS:")
for m in moedas:
    qtdeMoedas = int(valor / m)
    print(f"{qtdeMoedas} moeda(s) de R$ {m:.2f}")
    valor = valor - (qtdeMoedas * m)