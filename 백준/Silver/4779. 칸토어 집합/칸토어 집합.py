def ctr(s):
    if len(s) > 1:
        return ctr(s[:len(s) // 3]) + " " * (len(s) // 3) + ctr(s[(len(s) // 3) * 2:])
    else:
        return s

while True:
    try:
        n = int(input())
        a = "-" * 3 ** n
        print(ctr(a))
    except:
        break