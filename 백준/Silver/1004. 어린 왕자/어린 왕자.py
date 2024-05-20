T = int(input())
for i in range(T):
    escape = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for j in range(n):
        cx, cy, r = map(int, input().split())
        if (((((cx - x1) ** 2 + (cy - y1) ** 2) ** (1 / 2)) < r) and ((((cx - x2) ** 2 + (cy - y2) ** 2) ** (1 / 2)) > r)) or (((((cx - x1) ** 2 + (cy - y1) ** 2) ** (1 / 2)) > r) and ((((cx - x2) ** 2 + (cy - y2) ** 2) ** (1 / 2)) < r)):
            escape += 1
    print(escape)