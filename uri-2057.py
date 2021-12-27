saida, t_v, fuso = input().split()
saida = int(saida)
t_v = int(t_v)
fuso = int(fuso)
chegada = (saida + t_v + fuso)

if(chegada < 0):
    print(chegada + 24)
elif(chegada >= 24):
    print(chegada - 24)
elif(0 <= chegada < 24):
    print(chegada)

