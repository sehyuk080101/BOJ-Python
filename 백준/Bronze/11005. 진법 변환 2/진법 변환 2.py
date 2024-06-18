N, B = map(int, input().split())
a = [i for i in range(10)]
w = []
for i in range(10, B):
    a.append(chr(i + 55))
while N:
    w.append(a[N % B])
    N //= B
for i in range(len(w)):
    print(w[-(i + 1)], end="")