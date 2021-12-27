horaI, horaF = input().split()
horaI = int(horaI)
horaF = int(horaF)

tempo = horaF - horaI
if tempo <= 0:
    tempo = tempo + 24

print(f"O JOGO DUROU {tempo} HORAS(S)")