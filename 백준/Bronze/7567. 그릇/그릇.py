h = 10
p = list(input())
for i in range(1, len(p)):
    if p[i] == p[i - 1]:
        h += 5
    else:
        h += 10
print(h)