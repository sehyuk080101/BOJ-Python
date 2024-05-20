d = []
for i in range(28):
    a = int(input())
    d.append(a)
for j in range(1, 31):
    if j not in d:
        print(j, end=" ")