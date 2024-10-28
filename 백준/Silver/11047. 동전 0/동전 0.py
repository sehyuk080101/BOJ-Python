import sys

n, k = map(int, sys.stdin.readline().split())
l = []
cnt = 0
j = -1

for i in range(n):
    l.append(int(sys.stdin.readline()))

while k != 0:
    if k - l[j] >= 0:
        cnt += k // l[j]
        k %= l[j]
    else:
        j -= 1

print(cnt)