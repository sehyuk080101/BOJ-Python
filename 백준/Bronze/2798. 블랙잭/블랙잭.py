N, M = map(int, input().split())
m = 0
a = set(map(int, input().split()))
for i in a:
    for j in a - {i}:
        for k in a - {i, j}:
            if m < i + j + k <= M:
                m = i + j + k
print(m)