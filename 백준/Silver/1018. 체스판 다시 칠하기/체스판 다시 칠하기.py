n, m = map(int, input().split())
arr = []
mi = 64

for i in range(n):
    arr.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        wcnt = 0
        bcnt = 0
        for k in range(8):
            for l in range(8):
                if (k + i) % 2 == i % 2:
                    if (l + j) % 2 == j % 2:
                        if arr[k + i][l + j] == "W":
                            bcnt += 1
                        else:
                            wcnt += 1
                    else:
                        if arr[k + i][l + j] == "W":
                            wcnt += 1
                        else:
                            bcnt += 1
                else:
                    if (l + j) % 2 == j % 2:
                        if arr[k + i][l + j] == "W":
                            wcnt += 1
                        else:
                            bcnt += 1
                    else:
                        if arr[k + i][l + j] == "W":
                            bcnt += 1
                        else:
                            wcnt += 1

        if min(wcnt, bcnt) < mi:
            mi = min(wcnt, bcnt)
            
print(mi)