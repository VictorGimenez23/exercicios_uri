nome = input()
salario = float(input())
vendas = float(input())

comissao = ((vendas * 15) / 100) + salario

print(f"TOTAL = R$ {comissao:.2f}")