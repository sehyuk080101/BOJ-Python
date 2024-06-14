d = []
m = 0
for i in range(5):
    a = input()
    if len(a) > m:
        m = len(a)
    d.append(a)
for q in range(5):
    d[q] += " " * (m - len(d[q]))
for j in range(m):
    for k in range(5):
        if d[k][j] != " ":
            print(d[k][j], end="")