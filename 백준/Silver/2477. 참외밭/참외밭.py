k = int(input())
l = []
a = 0
b = 0

for i in range(6):
    c, d = map(int, input().split())
    l.append([c, d])

for i in range(6):
    if l[i][0] == l[(i + 2) % 6][0] and l[(i + 1) % 6][0] == l[(i + 3) % 6][0]:
        a = l[(i + 1) % 6][1] * l[(i + 2) % 6][1]
        b = (l[i][1] + l[(i + 2) % 6][1]) * (l[(i + 1) % 6][1] + l[(i + 3) % 6][1])
        break

print((b - a) * k)
