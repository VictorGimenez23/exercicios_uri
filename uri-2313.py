a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if(b == (a + c)):
    print("Invalido")
    if(a == (b + c)):
        print("Invalido")
    elif(c == (a + c)):
        print("Invalido")
elif(a==b or b==c or a==c):
    print("Valido-Isoceles")
    if (a ** 2 == (b ** 2 + c ** 2)):
        print("Retangulo: S")
    else:
        print("Retangulo: N")

elif( a != b and b != c and a != c):
    print("Valido-Escaleno")
    if (c ** 2 == (a ** 2 + b ** 2)):
        print("Retangulo: S")
    else:
        print("Retangulo: N")


