n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
res = 0

for i in range(len(a)):
    res += a[i] * b[i]

print(res)