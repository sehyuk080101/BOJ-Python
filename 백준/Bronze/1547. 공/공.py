M = int(input())
c = [1, 0, 0]
for i in range(M):
    X, Y = map(int, input().split())
    c[X - 1], c[Y - 1] = c[Y - 1], c[X - 1]
print(c.index(1) + 1)