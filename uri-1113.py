x = 0
y = 1

while( x != y):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if(x > y):
        print(f"Decrescente")
    elif(y > x):
        print(f"Crescente")
