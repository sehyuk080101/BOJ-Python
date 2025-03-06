def star(li, x, y, length):
    if length >= 3:
        c = length // 3

        for i in range(c):
            for j in range(c):
                li[x + c + i][y + c + j] = " "

        star(li, x, y, c)
        star(li, x, y + c, c)
        star(li, x, y + c * 2, c)
        star(li, x + c, y, c)
        star(li, x + c, y + c * 2, c)
        star(li, x + c * 2, y, c)
        star(li, x + c * 2, y + c, c)
        star(li, x + c * 2, y + c * 2, c)

n = int(input())
l = []

for _ in range(n):
    l.append(["*"] * n)

star(l, 0, 0, n)

for _ in range(n):
    for k in range(n):
        print(l[_][k], end="")
    print()