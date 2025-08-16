n = int(input())
count = 0

if n < 100:
    print(n)
else:
    for i in range(111, n + 1):
        tf = True
        s = str(i)
        d = int(s[0]) - int(s[1])

        for j in range(1, len(str(i)) - 1):
            if int(s[j]) - int(s[j + 1]) != d:
                tf = False
                break

        if tf:
            count += 1

    print(count + 99)
