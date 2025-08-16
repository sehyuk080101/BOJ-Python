l = [0] * 101
l[1], l[2], l[3], l[4] = 1, 1, 1, 2

for i in range(5, 101):
    l[i] = l[i - 1] + l[i - 5]

for _ in range(int(input())):
    print(l[int(input())])
