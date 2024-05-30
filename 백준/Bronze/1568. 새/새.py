n = int(input())
c = 0
k = 1
while n > 0:
    if k > n:
        k = 1
    n -= k
    k += 1
    c += 1
print(c)