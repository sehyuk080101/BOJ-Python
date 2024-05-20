N = int(input())
d = list(map(int, input().split()))
maxn = 0
res = 0
for i in d:
    if i > maxn:
        maxn = i
for j in range(N):
    d[j] = d[j] / maxn * 100
    res += d[j]
print(res/N)