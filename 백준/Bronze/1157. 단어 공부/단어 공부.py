d = {}
maxn = 0
same = 0
m = ""
a = input().upper()
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for j in d:
    if d[j] == maxn:
        same = d[j]
    if d[j] > maxn:
        maxn = d[j]
        m = j
if same == maxn:
    print("?")
else:
    print(m)