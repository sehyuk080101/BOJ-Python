n = int(input())
d = list(map(int, input().split()))
a = []

for i in d:
    tf = True
    if i == 1:
        continue
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            tf = False
            break
    if tf:
        a.append(i)
print(len(a))