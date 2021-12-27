n = int(input())

for i in range(n):
    x, y , z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)
    media = ((x * 2) + (y * 3) + (z * 5)) / (2 + 3 + 5)

    print(f"{media:.1f}")

