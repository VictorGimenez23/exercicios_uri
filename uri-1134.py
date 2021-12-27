qtdeAl = 0
qtdeGa = 0
qtdeDi = 0
while True:
    n = int(input())
    if(n == 1):
        qtdeAl = qtdeAl + 1

    elif(n == 2):
        qtdeGa = qtdeGa + 1

    elif(n == 3):
        qtdeDi = qtdeDi + 1

    elif(n == 4):
        break

print("MUITO OBRIGADO")
print(f"Alcool: {qtdeAl}")
print(f"Gasolina: {qtdeGa}")
print(f"Diesel: {qtdeDi}")
