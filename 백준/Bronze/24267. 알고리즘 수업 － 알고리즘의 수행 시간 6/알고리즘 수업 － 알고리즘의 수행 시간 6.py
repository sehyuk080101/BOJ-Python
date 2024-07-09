n = int(input())
res = 0
for i in range(n - 2):
    res += (n - (i + 1)) * (n - (i + 2)) // 2

print(str(res) + "\n" + "3")