n = int(input())
l = list(map(int, input().split()))
d = [1]

for i in range(1, n):
    m = 0
    for j in range(i):
        if l[j] < l[i] and d[j] > m:
            m = d[j]

    d.append(m + 1)

print(max(d))
