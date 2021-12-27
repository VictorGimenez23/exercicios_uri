n = int(input())

for i in range(n):
    x ,y = input().split()
    x = int(x)
    y = int(y)

    if(y != 0):
        divisao = x / y
        print(f"{divisao:.1f}")
    elif(y == 0):
        print(f"divisao impossivel")
