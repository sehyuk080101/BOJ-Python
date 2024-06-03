f = 0
s = 1
r = 1
for _ in range(int(input()) - 1):
    r = f + s
    s, f = r, s
print(r)