x = int(input())

while (x):
    if(x != 2002):
        print(f"Senha Invalida")
        x = int(input())
    elif(x == 2002):
        print(f"Acesso Permitido")
        break