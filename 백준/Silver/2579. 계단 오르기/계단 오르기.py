n = int(input())
l1 = [0] * (n + 1)
l2 = [0] * (n + 1)

for i in range(1, n + 1):
    l1[i] = int(input())

l2[1] = l1[1]

if n > 1:
    l2[2] = l2[1] + l1[2]

if n > 2:
    if l1[1] < l1[2]:
        l2[3] = l1[2] + l1[3]
    else:
        l2[3] = l1[1] + l1[3]

for i in range(4, n + 1):
    if l2[i - 2] < l2[i - 3] + l1[i - 1]:
        l2[i] = l2[i - 3] + l1[i - 1] + l1[i]
    else:
        l2[i] = l2[i - 2] + l1[i]

print(l2[n])
