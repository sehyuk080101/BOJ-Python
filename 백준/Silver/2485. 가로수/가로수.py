l = []
i = []
n = int(input())
res = 0
z = 0

for _ in range(n):
    l.append(int(input()))

for j in range(n - 1):
    i.append(l[j + 1] - l[j])

for j in range(len(i) - 1):
    if j == 0:
        a, b = i[j], i[j + 1]
    else:
        a, b = g, i[j + 1]
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    g = b
    z = g

for j in i:
    res += j // z - 1

print(res)