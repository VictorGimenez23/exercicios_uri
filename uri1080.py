n = int(input())
cont=0

for i in range(100):
    x = int(input())
    if (x > cont):
        maior = x
        posicao = i + 1
        cont = x

print(maior)
print(posicao)