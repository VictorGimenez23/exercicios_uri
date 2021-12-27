positivos = 0
soma = 0

for i in range(1,7):
    n = float(input())
    if(n > 0):
        positivos = positivos + 1
        soma = soma + n
media = soma / positivos
print(f"{positivos} valores positivos")
print(f"{media:.1f}")