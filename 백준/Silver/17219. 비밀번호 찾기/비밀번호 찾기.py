a, b = map(int, input().split())
d = {}
z = []
for _ in range(a):
    k, v = input().split()
    d[k] = v
for i in range(b):
    z.append(input())
for i in z:
    print(d[i])