n = int(input())
l = []
m = 0

for i in range(n):
    a, b = map(int, input().split())
    l.append([a, b])

sl = sorted(l, key=lambda x: (x[1], -x[0]))

v = set()
c = 0

for i in range(n):
    if sl[i][0] == sl[i][1]:
        m += 1
        c = sl[i][1]
        if i != n - 1 and sl[i][1] != sl[i + 1][1]:
            v.add(sl[i][1])
        continue
    if c in v and sl[i][0] < c:
        continue
    if not sl[i][1] in v:
        m += 1
        c = sl[i][1]
        v.add(sl[i][1])

print(m)
