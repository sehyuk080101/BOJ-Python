n = int(input())
l = []
o = 0
z = 0

for i in range(n):
    l.append(list(map(int, input().split())))

def paper(iterable, a):
    if a >= 1:
        b = a ** 2
        cnt = 0
        for j in range(a):
            for k in range(a):
                cnt += iterable[j][k]

        if cnt == b:
            global o
            o += 1
            return

        elif cnt == 0:
            global z
            z += 1
            return

        else:
            c = a // 2
            var1 = []
            for _ in range(c):
                var1.append(iterable[_][:c])
            paper(var1, c)
            var2 = []
            for _ in range(c):
                var2.append(iterable[_][c:])
            paper(var2, c)
            var3 = []
            for _ in range(c, a):
                var3.append(iterable[_][:c])
            paper(var3, c)
            var4 = []
            for _ in range(c, a):
                var4.append(iterable[_][c:])
            paper(var4, c)

paper(l, n)

print(z)
print(o)