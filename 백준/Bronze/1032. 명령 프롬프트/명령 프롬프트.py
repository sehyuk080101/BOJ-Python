for i in range(int(input())):
    w = list(input())
    if i != 0:
        for j in range(len(w)):
            if w[j] != c[j]:
                w[j] = "?"
    c = w
print("".join(c))