import sys

n = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))
li = []
result = 0


def m(l):
    index = 0
    value = 1000000001

    for i in range(len(l)):
        if l[i] < value:
            value = l[i]
            index = i

    return index


c = prices[:n - 1]

while True:
    a = m(c)
    li.append(a)
    c = c[:a]

    if a == 0:
        break

for i in range(len(li) - 1, -1, -1):
    b = li[i - 1]
    if i == 0:
        b = n - 1
    result += prices[li[i]] * sum(distances[li[i]:b])

print(result)
