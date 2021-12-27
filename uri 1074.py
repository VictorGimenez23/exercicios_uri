n = int(input())

for i in range(n):
    qtde = int(input())
    if(qtde < 0 and qtde % 2 != 0):
        print(f"ODD NEGATIVE")
    elif(qtde > 0 and qtde % 2 == 0):
        print(f"EVEN POSITIVE")
    elif(qtde > 0 and qtde % 2 != 0):
        print(f"ODD POSITIVE")
    elif(qtde == 0):
        print(f"NULL")
    elif(qtde < 0 and qtde % 2 == 0):
        print(f"EVEN NEGATIVE")

# l=[]
# a=int(input())
# for n in range(1,(a+1)):
#     l.append(int(input()))
# for n in l:
#     if (n%2!=0)and (n<0):
#         print("ODD NEGATIVE")
#     if(n==0):
#         print("NULL")
#     if(n%2!=0)and(n>0):
#         print("ODD POSITIVE")
#     if(n%2==0)and(n<0):
#         print("EVEN NEGATIVE")
#     if(n%2==0)and(n>0):
#         print("EVEN POSITIVE")