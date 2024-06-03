for _ in range(int(input())):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    else:
        print(a ** (b % 4 + 4) % 10)