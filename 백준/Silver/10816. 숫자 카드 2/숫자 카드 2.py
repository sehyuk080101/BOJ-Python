l = [0] * 20000001
n = int(input())
nl = list(map(int, input().split()))

for i in nl:
    l[i] += 1

m = int(input())
ml = list(map(int, input().split()))

for i in ml:
    print(l[i], end=" ")