while True:
    s = 0
    n = input()
    if int(n) == 0:
        break
    for i in range(len(n) // 2):
        if n[i] != n[-(i + 1)]:
            s += 1
    if s == 0:
        print("yes")
    else:
        print("no")