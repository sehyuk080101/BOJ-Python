m, n = map(int, input().split())
if m < 2:
    m = 2

l = [True] * (n + 1)
l[0], l[1] = False, False

i = 2
while i < n:
    for j in range(i * 2, n + 1, i):
        l[j] = False
    for j in range(i + 1, n + 1):
        i += 1
        if l[i]:
            break

for i in range(m, n + 1):
    if l[i]:
        print(i)