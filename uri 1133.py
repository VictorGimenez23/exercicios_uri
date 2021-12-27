x = int(input())
y = int(input())

for i in range(x,y):
    if(x and y > 0):
        if(i % 5 == 2 or i % 5 == 3):
            print(f"{i}")