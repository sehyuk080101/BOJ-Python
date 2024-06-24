for _ in range(int(input())):
    s = input()
    if s == s[::-1]:
        print(1, len(s) // 2 + 1)
    else:
        i = 1
        for j in range(len(s) // 2):
            if s[j] != s[-(j + 1)]:
                break
            i += 1
        print(0, i)