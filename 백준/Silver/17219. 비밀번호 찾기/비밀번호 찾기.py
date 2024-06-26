import sys

a, b = map(int, sys.stdin.readline().split())
d = {}
for _ in range(a):
    k, v = sys.stdin.readline().split()
    d[k] = v
for _ in range(b):
    print(d[sys.stdin.readline().strip()])