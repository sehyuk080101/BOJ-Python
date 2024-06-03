x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
if x[0] == x[1]:
    a4 = x[2]
else:
    a4 = x[0]
if y[0] == y[1]:
    b4 = y[2]
else:
    b4 = y[0]
print(a4, b4)