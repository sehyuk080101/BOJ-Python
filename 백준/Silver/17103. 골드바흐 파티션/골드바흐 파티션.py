l = [True] * 1000001
l[0], l[1] = False, False

i = 2
while i < 1000000:
    for j in range(i * 2, 1000001, i):
        l[j] = False
    for j in range(i + 1, 1000001):
        i += 1
        if l[i]:
            break

for _ in range(int(input())):
    n = int(input())
    cnt = 0

    for i in range(2, n // 2 + 1):
        if l[i] and l[n - i]:
            cnt += 1

    print(cnt)