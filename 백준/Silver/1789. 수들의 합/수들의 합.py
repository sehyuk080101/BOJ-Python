N = int(input())
i = 0
cnt = 0
while N > 0:
    i += 1
    cnt += 1
    if N - (i * 2 + 1) < 0:
        break
    else:
        N -= i
print(cnt)