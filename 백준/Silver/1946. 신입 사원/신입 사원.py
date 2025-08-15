import sys

for _ in range(int(sys.stdin.readline())):
    count = 1
    n = int(sys.stdin.readline())
    l = []

    for i in range(n):
        l.append(list(map(int, sys.stdin.readline().split())))

    l.sort(key=lambda x: x[0])
    s = l[0][1]

    for i in range(1, n):
        if s > l[i][1]:
            s = l[i][1]
            count += 1

    print(count)
