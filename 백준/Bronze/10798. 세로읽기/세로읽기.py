d = []
for i in range(5):
    d.append(input())
leng = 0
for k in range(len(d)):
    if len(d[k]) > leng:
        leng = len(d[k])
for m in range(len(d)):
    d[m] += " "*(leng-len(d[m]))
for j in range(leng):
    for n in range(len(d)):
        if d[n][j] != " ":
            print(d[n][j], end="")