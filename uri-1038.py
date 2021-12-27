codigo, qtde = input().split()
codigo = int(codigo)
qtde = int(qtde)

if codigo == 1:
    total = 4.00 * qtde
    print(f"Total: R$ {total:.2f}")
elif codigo == 2:
    total = 4.50 * qtde
    print(f"Total: R$ {total:.2f}")
elif codigo == 3:
    total = 5.00 * qtde
    print(f"Total: R$ {total:.2f}")
elif codigo == 4:
    total = 2.00 * qtde
    print(f"Total: R$ {total:.2f}")
elif codigo == 5:
    total = 1.50 * qtde
    print(f"Total: R$ {total:.2f}")