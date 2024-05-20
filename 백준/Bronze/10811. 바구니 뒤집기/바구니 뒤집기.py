N, M = map(int, input().split())
d = list(range(1, N + 1))
for z in range(M):
    i, j = map(int, input().split())
    if (i - j + 1) % 2 == 0:
        for k in range(int((j - i + 1) / 2)):
            d[i + k - 1], d[j - k - 1] = d[j - k - 1], d[i + k - 1]
    else:
        for k in range(int((j - i + 1) / 2 + 1)):
            d[i + k - 1], d[j - k - 1] = d[j - k - 1], d[i + k - 1]
print(*d)