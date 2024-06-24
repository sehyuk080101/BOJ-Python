m = int(input())
n = int(input())
d = []
for i in range(m, n + 1):
    tf = True
    if i == 1:
        continue
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            tf = False
            break
    if tf:
        d.append(i)
if d:
    print(sum(d))
    print(d[0])
else:
    print(-1)