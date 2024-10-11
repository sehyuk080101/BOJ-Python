import sys

l = []
n = int(sys.stdin.readline())

for i in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

for i in reversed(l):
    print(i)