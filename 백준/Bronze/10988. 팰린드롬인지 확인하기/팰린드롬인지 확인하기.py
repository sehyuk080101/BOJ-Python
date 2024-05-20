a = input()
res = 0
for i in range(int(len(a) / 2)):
    if a[i] != a[-(i + 1)]:
        res += 1
if res:
    print(0)
else:
    print(1)