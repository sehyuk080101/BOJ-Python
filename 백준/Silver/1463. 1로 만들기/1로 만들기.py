n = int(input())
d = {1: 0, 2: 1, 3: 1}

for i in range(4, n + 1):
    l = [d[i - 1]]
    if i % 2 == 0:
        l.append(d[i // 2])
    if i % 3 == 0:
        l.append(d[i // 3])
    d[i] = min(l) + 1

print(d[n])
