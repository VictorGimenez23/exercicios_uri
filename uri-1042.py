a, b ,c = input().split()
a = int(a)
b = int(b)
c = int(c)

posicao = [a,b,c]
posicao.sort()

print(f"{posicao[0]}")
print(f"{posicao[1]}")
print(f"{posicao[2]}\n")
print(f"{a}")
print(f"{b}")
print(f"{c}")