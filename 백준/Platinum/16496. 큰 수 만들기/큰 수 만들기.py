n = int(input())
li = input().split()
res = ""

for i in range(n - 1, 0, -1):
    for j in range(i):
        if int(li[j + 1] + li[j]) > int(li[j] + li[j + 1]):
            li[j], li[j + 1] = li[j + 1], li[j]

for i in li:
    res += i

print(int(res))