res = 0
for _ in range(5):
    n = int(input())
    if n <= 40:
        n = 40
    res += n
print(res // 5)