i = 0
n = int(input())
while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n += 1
    i += 1
print(i)