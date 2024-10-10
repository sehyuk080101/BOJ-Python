import sys

n = int(sys.stdin.readline())
l = [0] * 8001
m = 0
b = -4000
c = 4000
d = 0
e = []
f = 0

for i in range(n):
    a = int(sys.stdin.readline())
    m += a
    l[a + 4000] += 1
    if a > b:
        b = a
    if a < c:
        c = a

for i in range(len(l)):
    if l[i] > d:
        d = l[i]
        f = i - 4000
    if l[i] != 0:
        for j in range(l[i]):
            e.append(i - 4000)

for i in range(f + 4001, len(l)):
    if l[i] == l[f + 4000]:
        f = i - 4000
        break

if m / n % 1 >= 0.5:
    print(m // n + 1)
else:
    print(m // n)
print(e[len(e) // 2])
print(f)
print(b - c)