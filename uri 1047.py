horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()
horaInicial = int(horaInicial)
minutoInicial = int(minutoInicial)
horaFinal = int(horaFinal)
minutoFinal = int(minutoFinal)

horas = horaFinal - horaInicial

if(horas < 0):
    horas = horas + 24

minutos = minutoFinal - minutoInicial

if(minutos < 0):
    minutos = minutos + 60
    horas = horas - 1

if(horas == 0 and minutos == 0):
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif(horas != 0 and minutos != 0):
    print(f" O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")




exit()
# horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()
# horaInicial = int(horaInicial)
# minutoInicial = int(minutoInicial)
# horaFinal = int(horaFinal)
# minutoFinal = int(minutoFinal)
#
# diferenca = ((horaFinal * 60) + minutoFinal) - ((horaInicial * 60) + minutoInicial)
# #hora final e minuto final antes, para o resultado ser negativo
# if(diferenca <= 0):
#     diferenca = diferenca + (24 * 60)
#     hora = diferenca // 60
#     minuto = diferenca % 60
#
# print(f"O JOGO DUROU {hora} HORAS(S) E {minuto} MINUTOS(S)")