import sys

for _ in range(int(sys.stdin.readline())):
    escape = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(int(sys.stdin.readline())):
        cx, cy, r = map(int, sys.stdin.readline().split())
        d1 = ((cx - x1) ** 2 + (cy - y1) ** 2) ** (1 / 2)
        d2 = ((cx - x2) ** 2 + (cy - y2) ** 2) ** (1 / 2)
        if (d1 > r and d2 < r) or (d1 < r and d2 > r):
            escape += 1
    sys.stdout.write(str(escape) + "\n")