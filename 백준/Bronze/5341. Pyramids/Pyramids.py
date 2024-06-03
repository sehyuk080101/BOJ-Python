while True:
    res = 0
    n = int(input())
    if not(n):
        break
    for i in range(n, 0, -1):
        res += i
    print(res)