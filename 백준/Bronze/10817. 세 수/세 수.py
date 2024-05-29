n = list(map(int, input().split()))
n.remove(max(n))
n.remove(min(n))
print(*n)