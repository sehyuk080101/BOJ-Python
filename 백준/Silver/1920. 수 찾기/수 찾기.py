d = {}
n = int(input())
nl = list(map(int, input().split()))
m = int(input())
ml = list(map(int, input().split()))

for i in nl:
    if i not in d:
        d[i] = True

for i in ml:
    if i in d:
        print(1)
    else:
        print(0)
