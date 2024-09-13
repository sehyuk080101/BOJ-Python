m, n = map(int, input().split())
if m < 2:
    m = 2

l = [True] * (n + 1)
l[0], l[1] = False, False

j = 2
for i in range(2, n + 1):
    for k in range(j * 2, n + 1, j):
        l[k] = False
    for k in range(j + 1, n + 1):
        if l[k]:
            j = k
            break

for i in range(m, n + 1):
    if l[i]:
        print(i)