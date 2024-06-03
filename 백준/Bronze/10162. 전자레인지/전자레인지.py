t = int(input())
s = [0, 0, 0]
while True:
    if t >= 300:
        t -= 300
        s[0] += 1
    elif t >= 60:
        t -= 60
        s[1] += 1
    else:
        t -= 10
        s[2] += 1
    if t == 0:
        print(*s)
        break
    elif t < 0:
        print(-1)
        break