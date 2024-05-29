for i in range(int(input())):
    s = 0
    n = input()
    for j in range(len(n)):
        if n[j] == "1":
            s += 2 ** (23 - j)
    print(s)