w = ""
r = ""
m = 0
while True:
    try:
        w += input()
    except:
        break
alp = {}
for i in w:
    if i != " ":
        if i not in alp:
            alp[i] = 0
        alp[i] += 1
for k, v in sorted(alp.items()):
    if v > m:
        r = k
        m = v
    elif v == m:
        r += k
print(r)