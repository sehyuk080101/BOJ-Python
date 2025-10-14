import copy

n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

dp = copy.deepcopy(l)

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        if dp[i + 1][j] > dp[i + 1][j + 1]:
            dp[i][j] = dp[i + 1][j] + l[i][j]
        else:
            dp[i][j] = dp[i + 1][j + 1] + l[i][j]

print(dp[0][0])
