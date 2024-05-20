d = []
maxnum = 0
maxmaxnum = 0
for i in range(1, 10):
    a = int(input())
    d.append(a)
    if a > maxnum:
        maxnum = a
        maxmaxnum = i
print(max(d))
print(maxmaxnum)