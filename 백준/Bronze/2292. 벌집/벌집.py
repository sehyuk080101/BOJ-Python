n = int(input())
i = 1
r = 1
if n == 1:
    print(1)
else:
    while True:
        if r + 1 <= n <= r + 6 * i:
            break
        r += 6 * i
        i += 1
    print(i + 1)