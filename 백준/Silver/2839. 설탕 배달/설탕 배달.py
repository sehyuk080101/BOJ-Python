N = int(input())
num = 0
while True:
    if N % 5 == 0:
        print(num + int(N / 5))
        break
    else:
        N -= 3
        num += 1
    if N < 0:
        print(-1)
        break