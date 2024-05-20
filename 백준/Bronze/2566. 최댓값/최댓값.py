d = []
maxnum = 0
coor = [0, 0]
for i in range(9):
    d.append(list(map(int, input().split())))
for j in range(len(d)):
    for k in range(len(d[j])):
        if d[j][k] >= maxnum:
            maxnum = d[j][k]
            coor = [j + 1, k + 1]
print(maxnum)
print(*coor)