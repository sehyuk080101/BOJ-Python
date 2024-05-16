z = 0
n = int(input())
a = list(map(int, input().split()))
b = int(input())
for j in range(n):
    if b == a[j]:
        z += 1
print(z)