n = int(input())
d = []
m = [1]
x = 0
y = 1
for _ in range(int(input())):
    a, b = map(int, input().split())
    d.append([a, b])
while x != y:
    y = x
    for i in d:
        for j in range(len(i)):
            if i[j] in m:
                if i[j - 1] not in m:
                    m.append(i[j - 1])
                i[j - 1], i[j] = 0, 0
                y += 1
print(len(m) - 1)