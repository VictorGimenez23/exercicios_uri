a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if (b ** 2 - 4 * a * c) < 0 or (a == 0.0):
    print(f"Impossivel calcular")

else:
    x1 = (- b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x2 = (- b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
