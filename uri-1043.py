a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a + b > c > (a - b) and c + a > b > (c - a) and b + c > a > (b - c):
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")