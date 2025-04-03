import sys

l = [0] * 20000001
n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))

for i in nl:
    l[i] += 1

m = int(sys.stdin.readline())
ml = list(map(int, sys.stdin.readline().split()))

for i in ml:
    print(l[i], end=" ")