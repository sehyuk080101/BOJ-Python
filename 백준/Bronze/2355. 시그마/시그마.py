A, B = map(int, input().split())
n1 = min(A, B)
n2 = max(A, B)
print((n1 + n2) * (n2 - n1 + 1) // 2)