h = []
for _ in range(9):
    h.append(int(input()))
r = False
for i in range(8):
    for j in range(i + 1, 9):
        if sum(h) - (h[i] + h[j]) == 100:
            for k in sorted(h):
                if k != h[i] and k != h[j]:
                    print(k)
                    r = True
    if r:
        break