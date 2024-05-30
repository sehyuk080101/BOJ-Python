oct = {"-" : 0, "\\" : 1, "(" : 2, "@" : 3, "?" : 4, ">" : 5, "&" : 6, "%" : 7, "/" : -1}
while True:
    s = 0
    w = input()
    if w == "#":
        break
    for i in range(len(w)):
        s += oct[w[i]] * 8 ** (len(w) - (i + 1))
    print(s)