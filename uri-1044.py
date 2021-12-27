a, b = input().split()
a = int(a)
b = int(b)

if (a % b == 0) or (b % a == 0):
    print(f"Sao Multiplos")
elif (a % b != 0) or (b % a != 0):
    print(f"Nao sao multiplos")