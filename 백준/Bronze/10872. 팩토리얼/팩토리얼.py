n = int(input())
if not(n):
    print(1)
else:
    for i in range(n - 1, 0, -1):
        n *= i
    print(n)