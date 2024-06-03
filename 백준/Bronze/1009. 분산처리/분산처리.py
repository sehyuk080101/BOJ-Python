for _ in range(int(input())):
    a, b = map(int, input().split())
    a = a % 10
    n = 0
    if a == 0:
        print(10)
        n += 1
    elif b == 1:
        print(a)
        n += 1
    elif b == 2:
        print(a ** b % 10)
        n += 1
    else:
        for i in range(1, b + 1):
            if a == a ** (i + 1) % 10:
                if b % i == 0:
                    print(a ** i % 10)
                else:
                    print(a ** (b % i) % 10)
                n += 1
                break
    if not(n):
        print(a ** b % 10)