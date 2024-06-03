for i in range(int(input())):
    a = 1
    b = 0
    for _ in range(int(input())):
        a, b = b, a + b
    print(a, b)