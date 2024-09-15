while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    l = [True] * (n * 2 + 1)
    l[0], l[1] = False, False
    i = 2
    while i < n * 2:
        for j in range(i * 2, n * 2 + 1, i):
            l[j] = False
        for j in range(i + 1, n * 2 + 1):
            i += 1
            if l[i]:
                break
    for i in l[n + 1:n * 2 + 1]:
        if i:
            cnt += 1
    print(cnt)