a = 1
b = 1
c = 1
while (True):
    a, b ,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    x = int(input())
    x = a,b,c

    if(a == 0):
        break

    area = a * b
    terreno = (area * 100) / c
    terreno = terreno ** (1 / 2)
    print(f"{round(terreno)}")





exit()
qtde = 0
n = 0
media = 0
soma = 0
while(n >= 0):
    n = int(input())
    if(n >= 0):
        soma = soma + n
        qtde = qtde + 1
        media = soma / qtde
    elif(n < 0):
        break

print(f"{media:.2f}")