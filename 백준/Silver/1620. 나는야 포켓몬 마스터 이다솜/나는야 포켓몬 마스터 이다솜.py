n, m = map(int, input().split())
p = {}
for i in range(1, n + 1):
    s = input()
    p[s] = i
    p[str(i)] = s
for i in range(m):
    print(p[input()])