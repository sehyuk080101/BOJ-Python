N, M = map(int, input().split())
d = []
for _ in range(N):
    d.append(0)
for _ in range(M):
    i, j, k = map(int, input().split())
    for z in range(i, j + 1):
        d[z - 1] = k
print(*d)