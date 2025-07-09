n = int(input())
a = 0

while n > 0:
    if n % 3 == 0:
        n -= 3
    else:
        n -= 1
    a += 1

if a % 2 == 0:
    print("CY")
else:
    print("SK")
