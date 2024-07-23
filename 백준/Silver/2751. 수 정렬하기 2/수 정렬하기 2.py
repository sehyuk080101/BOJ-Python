import sys

arr = []

n = int(sys.stdin.readline())

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
    sys.stdout.write(str(i) + "\n")