x, y = input().split()
x = float(x)
y = float(y)

if (x == y == 0):
    print(f"Origem")
elif(x == 0):
    print(f"Eixo X")
elif(y ==0):
    print(f"Eixo Y")
elif (x > 0) and (y > 0):
    print(f"Q1")
elif (x < 0) and (y > 0):
    print(f"Q2")
elif (x < 0) and (y < 0):
    print(f"Q3")
elif (x > 0) and (y < 0):
    print(f"Q4")