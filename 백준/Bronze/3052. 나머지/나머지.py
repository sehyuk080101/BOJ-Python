d = []
num = 0
for i in range(10):
    n = int(input())
    if n % 42 not in d:
        num += 1
        d.append(n % 42)
print(num)