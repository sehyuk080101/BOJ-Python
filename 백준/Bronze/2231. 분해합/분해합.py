n = int(input())
res = 0
for i in range(n):
    s = i
    for j in str(i):
        s += int(j)
    if s == n:
        res = i
        break
print(res)