import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    l = []

    for i in range(n):
        l.append(list(map(int, sys.stdin.readline().split())))

    l.sort(key=lambda x: x[0])
    s = [l[0][1]]

    for i in range(1, n):
        if s[-1] > l[i][1]:
            s.append(l[i][1])

    print(len(s))
