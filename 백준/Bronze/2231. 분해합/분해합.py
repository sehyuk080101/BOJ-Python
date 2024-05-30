N = int(input())
res = 0
for i in range(N):
    s = i
    for j in str(i):
        s += int(j)
    if s == N:
        res = i
        break
print(res)