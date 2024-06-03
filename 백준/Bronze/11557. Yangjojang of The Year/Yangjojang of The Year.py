for _ in range(int(input())):
    s = {}
    for i in range(int(input())):
        sc, n = input().split()
        s[int(n)] = sc
    print(s[max(s)])