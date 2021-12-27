salario = float(input())

if(salario >= 0 and salario <= 400.00):
    salarioNovo = salario + ((15 / 100) * salario)
    reajuste = 15 / 100 * salario

    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 15 %")

elif(salario >= 400.01 and salario <= 800.00):
    salarioNovo = salario + ((12 / 100) * salario)
    reajuste = 12 /100 * salario

    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 12 %")

elif(salario >= 800.01 and salario <= 1200.00):
    salarioNovo = salario + ((10 / 100) * salario)
    reajuste = 10 / 100 * salario

    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 10 %")

elif(salario >= 1200.01 and salario <= 2000.00):
    salarioNovo = salario + ((7 / 100) * salario)
    reajuste = 7 / 100 * salario

    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 7 %")

elif(salario > 2000.00):
    salarioNovo = salario + ((4 / 100) * salario)
    reajuste = 4 / 100 * salario

    print(f"Novo salario: {salarioNovo:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: 4 %")