pares = 0
for i in range(5):
    n = int(input())
    if( n % 2 == 0):
        pares = pares + 1
print(f"{pares} valores pares")