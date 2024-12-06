for _ in range(int(input())):
    p = 0
    a = input()
    b = 1
    for i in a:
        if i == "O":
            p += b
            b += 1
        else:
            b = 1
    print(p)