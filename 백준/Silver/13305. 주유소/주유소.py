import sys

n = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))
result = distances[0] * prices[0]
m = prices[0]

for i in range(1, n - 1):
    if prices[i] < m:
        m = prices[i]

    result += m * distances[i]

print(result)
