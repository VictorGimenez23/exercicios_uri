valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]

print(f"{valor}")
for c in cedulas:
    qtdeCedulas = int(valor / c)
    print(f"{qtdeCedulas} nota(s) de R$ {c},00")
    valor = valor - (qtdeCedulas * c)