n = int(input())
d = {}

for i in range(n):
    s = input().split()
    if s[0] not in d:
        d[s[0]] = 0
    if s[1] == "enter":
        d[s[0]] += 1
    else:
        d[s[0]] -= 1

for i in sorted(d, reverse=True):
    if d[i] == 1:
        print(i)