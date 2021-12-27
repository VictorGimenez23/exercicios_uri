n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    for numero in range(x, y):
        if(x % 2 != 0):
            print(f"{x + numero}")