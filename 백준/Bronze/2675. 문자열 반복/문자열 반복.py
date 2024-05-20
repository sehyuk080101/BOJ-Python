T = int(input())
for i in range(T):
    d = ""
    a = input().split()
    for j in a[1]:
        d += j * int(a[0])
    print(d)