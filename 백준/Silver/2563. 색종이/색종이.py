d = [[0 for i in range(100)] for j in range(100)]
num = 0
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    for k in range(10):
        for j in range(10):
            d[x - k][y + j] = 1
for i in range(100):
    for j in range(100):
        if d[i][j]:
            num += 1
print(num)