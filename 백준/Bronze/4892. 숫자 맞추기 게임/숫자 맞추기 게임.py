i = 0
while True:
    i += 1
    n = int(input())
    if not(n):
        break
    if n % 2 == 0:
        print(f"{i}. even {int(n / 2)}")
    else:
        print(f"{i}. odd {int((n - 1) / 2)}")