T = int(input())
s = 0
a = list(map(int, input().split()))
for i in a:
    if i == T:
        s += 1
print(s)