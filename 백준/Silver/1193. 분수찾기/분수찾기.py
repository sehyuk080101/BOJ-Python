n = int(input())
i = 2
r = 1

while n > r:
    r += i
    i += 1

if i % 2 == 0:
    print(f"{r - n + 1}/{i - r + n - 1}")
else:
    print(f"{i - r + n - 1}/{r - n + 1}")