n = 0
N = int(input())
for i in range(N):
    d = []
    a = input()
    num = 0
    word = a[0]
    for j in a:
        if j != word:
            if j in d:
                num += 1
            d.append(word)
        word = j
    if num == 0:
        n += 1
print(n)