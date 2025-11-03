l = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    for i in range(1, k + 1):
        l.append([])
        for j in range(1, 15):
            l[i].append(sum(l[i - 1][:j]))

    print(l[k][n - 1])
