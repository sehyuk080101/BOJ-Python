while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if max(a, b, c) == a:
        if b ** 2 + c ** 2 == a ** 2:
            print("right")
        else:
            print("wrong")
    elif max(a, b, c) == b:
        if a ** 2 + c ** 2 == b ** 2:
            print("right")
        else:
            print("wrong")
    else:
        if a ** 2 + b ** 2 == c ** 2:
            print("right")
        else:
            print("wrong")