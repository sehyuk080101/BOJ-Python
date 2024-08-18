a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = a * d + c * b, b * d
g, h = e, f

if e > f:
    e, f = f, e
while e % f != 0:
    e, f = f, e % f

print(g // f, h // f)