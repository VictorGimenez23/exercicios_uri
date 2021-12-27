x = 1
y = 1

while(x != 0 or y != 0):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if(x > 0 and y > 0):
        print(f"primeiro")
    elif(x > 0 and y < 0):
        print(f"quarto")
    elif(x < 0 and y > 0):
        print(f"segundo")
    elif(x < 0 and y < 0):
        print(f"terceiro")
