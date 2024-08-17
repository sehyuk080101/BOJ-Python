d = {}
n, m = map(int, input().split())
nl = list(map(int, input().split()))
ml = list(map(int, input().split()))
res = 0

for i in nl:
    d[i] = 1

for i in ml:
    if i in d:
        d[i] = 0
    else:
        d[i] = 1

for i in d:
    res += d[i]

print(res)