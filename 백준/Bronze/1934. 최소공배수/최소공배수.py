for _ in range(int(input())):
    a, b = map(int, input().split())
    c, d = a, b
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    print(c * d // b)