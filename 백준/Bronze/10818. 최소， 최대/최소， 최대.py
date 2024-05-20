minnum = 1000001
maxnum = -1000001
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] > maxnum:
        maxnum = a[i]   
    if a[i] < minnum:
        minnum = a[i]
print(minnum, maxnum)