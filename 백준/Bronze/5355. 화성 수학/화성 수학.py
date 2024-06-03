for _ in range(int(input())):
    s = input().split()
    res = float(s[0])
    for i in s[1:]:
        if i == "@":
            res *= 3
        elif i == "%":
            res += 5
        else:
            res -= 7
    print(f"{res:.2f}")