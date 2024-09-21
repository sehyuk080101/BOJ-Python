import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
j = 0

for i in range(n):
    print(j + 1)
    a = l[j]
    l[j] = 0
    if i == n - 1:
        break
    if a > 0:
        cnt = 0
        while True:
            if cnt == a:
                break
            if j == n - 1:
                j = 0
            else:
                j += 1
            if l[j] != 0:
                cnt += 1
    else:
        cnt = 0
        while True:
            if cnt == a:
                break
            if j == 0:
                j = n - 1
            else:
                j -= 1
            if l[j] != 0:
                cnt -= 1