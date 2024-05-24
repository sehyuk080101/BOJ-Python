N, M = map(int, input().split())
m = 0
a = list(map(int, input().split()))
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if m < a[i] + a[j] + a[k] <= M:
                m = a[i] + a[j] + a[k]
print(m)