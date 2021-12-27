palavra1 = input ()
palavra2 = input ()
palavra3 = input ()

if(palavra1 == "vertebrado"):
    if(palavra2 == "mamifero"):
        if(palavra3 == "onivoro"):
            print("homem")
        elif(palavra3 == "herbivoro"):
            print("vaca")
    elif(palavra2 == "ave"):
        if(palavra3 == "carnivoro"):
            print("aguia")
        elif(palavra3 == "onivoro"):
            print("pomba")

elif(palavra1 == "invertebrado"):
    if(palavra2 == "analideo"):
        if(palavra3 == "hematofago"):
            print("sanguessuga")
        elif(palavra3 == "onivoro"):
            print("minhoca")
    elif(palavra2 == "inseto"):
        if(palavra3 == "hematofago"):
            print("pulga")
        elif(palavra3 == "herbivoro"):
            print("lagarta")