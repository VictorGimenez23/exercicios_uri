numero = int(input())
dentro = 0
fora = 0
for i in range(numero):
    x = int(input())
    if (x >=10 and x <= 20):
        dentro = dentro + 1
    else:
        fora = fora + 1
print(f"{dentro} in")
print(f"{fora} out")