l = [True] * 10001

i = 1
while i < 10001:
    n = i

    for j in range(len(str(i))):
        n += int(str(i)[j])

    if n < 10001:
        l[n] = False

    i += 1

for i in range(1, len(l)):
    if l[i]:
        print(i)
