N = int(input())
d = {}
for i in range(N):
    a, b = input().split()
    b = int(b)
    d[b] = a
print(d[sorted(d)[0]])