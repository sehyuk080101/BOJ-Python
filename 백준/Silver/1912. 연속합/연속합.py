n = int(input())
l = list(map(int, input().split()))
dp = [0] * n
dp[0] = l[0]

for i in range(1, n):
    if dp[i - 1] > 0:
        dp[i] = dp[i - 1] + l[i]
    else:
        dp[i] = l[i]

print(max(dp))
