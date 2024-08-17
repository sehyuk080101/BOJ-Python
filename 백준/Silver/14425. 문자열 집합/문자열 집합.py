n, m = map(int, input().split())
s = {}
d = []
res = 0

for i in range(n):
    s[input()] = 0

for i in range(m):
    d.append(input())

for i in d:
    if i in s:
        res += 1

print(res)