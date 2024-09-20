n, k = map(int, input().split())
queue = [i for i in range(1, n + 1)]
l = []
i = 0
while len(l) != n:
    cnt = 0
    while True:
        if queue[i] != 0:
            cnt += 1
        if cnt == k:
            l.append(queue[i])
            queue[i] = 0
            break
        i = (i + 1) % n

print("<", end="")
print(*l, sep=", ", end="")
print(">")