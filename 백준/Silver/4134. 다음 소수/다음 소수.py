for _ in range(int(input())):
    n = int(input())
    if n <= 1:
        print(2)
        continue
    i = 2
    while True:
        tf = True
        while i ** 2 <= n:
            if n % i == 0:
                i = 2
                tf = False
                break
            i += 1
        if tf:
            print(n)
            break
        n += 1