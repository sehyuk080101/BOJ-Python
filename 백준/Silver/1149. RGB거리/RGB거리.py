n = int(input())
d = []
l = []

for i in range(n):
    a, b, c = map(int, input().split())
    l.append([a, b, c])

d.append(l[0])

for i in range(1, n):
    d.append([min(d[i - 1][1], d[i - 1][2]) + l[i][0], min(d[i - 1][0], d[i - 1][2]) + l[i][1], min(d[i - 1][0], d[i - 1][1]) + l[i][2]])

print(min(d[n - 1]))
