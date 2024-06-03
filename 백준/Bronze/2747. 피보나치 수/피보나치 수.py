a = 0
b = 1
f = 1
for _ in range(int(input()) - 1):
    f = a + b
    b, a = f, b
print(f)