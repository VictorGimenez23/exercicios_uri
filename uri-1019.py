n = int(input())

calculo = 60 * 60
horas = n // calculo
n = n % (calculo)
minutos = n // 60
n = n % 60

print(f"{horas}:{minutos}:{n}")
