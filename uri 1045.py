# a, b, c = list (map (float, input (). split ()))
# if (a < b):
#     temp = a
#     a = b
#     b = temp
# if (b < c):
#     temp = b
#     b = c
#     c = temp
# if (a < b):
#     temp = a
#     a = b
#     b = temp
# if (a >= (b + c)):
#     print("NAO FORMA TRIANGULO")
# elif (a * a == (b * b + c * c)):
#     print("TRIANGULO RETANGULO")
# elif (a * a> (b * b + c * c)):
#     print("TRIANGULO OBTUSANGULO")
# elif (a * a <(b * b + c * c)):
#     print("TRIANGULO ACUTANGULO")
# if (a == b and b == c):
#     print("TRIANGULO EQUILATERO")
# elif (a == b or b == c):
#     print("TRIANGULO ISOSCELES")
#
# exit()
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

ordem = [a,b,c]
ordem.sort(reverse = True)
a = float(ordem[0])

x = True

if (a >= (b + c)):
    print(f"NAO FORMA TRIANGULO")
    x = False
elif (a * a == (b * b + c * c) and x):
    print(f"TRIANGULO RETANGULO")
elif (a * a > (b * b + c * c) and x):
    print("TRIANGULO OBTUSANGULO")
elif (a * a < (b * b + c * c) and x):
    print("TRIANGULO ACUTANGULO")
elif (a == b and b == c and x):
    print(f"TRIANGULO EQUILATERO")
elif (a == b or b == c) and not (a == b or b == c) and x:
    print(f"TRIANGULO ISOSCELES")