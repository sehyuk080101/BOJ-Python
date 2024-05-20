N, M = map(int, input().split())
d = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    d[i - 1], d[j - 1] = d[j - 1], d[i - 1]
print(*d)