v = ["a", "e", "i", "o", "u"]
for i in range(int(input())):
    n = 0
    w = input().lower()
    w = w.replace(" ", "")
    for j in w:
        if j in v:
            n += 1
    print(len(w) - n, n)