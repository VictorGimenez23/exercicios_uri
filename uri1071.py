x = int(input())
y = int(input())
soma = 0
for v in range(( y + 1 ),x):
    if (v % 2 == 1):
        soma = soma + v
print(soma)