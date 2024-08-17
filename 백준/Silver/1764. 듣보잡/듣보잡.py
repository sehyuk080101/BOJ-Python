from unittest import defaultTestLoader

n, m = map(int, input().split())
d = {}
res = 0

for i in range(n):
    d[input()] = 0

for i in range(m):
    s = input()
    if s in d:
        d[s] += 1
        res += 1

print(res)
for i in sorted(d):
    if d[i] == 1:
        print(i)