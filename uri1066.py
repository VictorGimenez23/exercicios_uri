pares = 0
impares = 0
negativos = 0
positivos = 0

for x in range(5):
    n = int(input())
    if( n % 2 == 0 ):
        pares = pares + 1
    else:
        impares = impares + 1
    if(n > 0 ):
        positivos = positivos + 1
    elif(n < 0):
        negativos = negativos + 1

print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")