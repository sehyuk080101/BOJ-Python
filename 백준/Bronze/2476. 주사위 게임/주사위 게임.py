m = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        m.append(10000 + a * 1000)
    elif a == b:
        m.append(1000 + a * 100)
    elif b == c:
        m.append(1000 + b * 100)
    elif c == a:
        m.append(1000 + c * 100)
    else:
        m.append(max(a, b, c) * 100)
print(max(m))