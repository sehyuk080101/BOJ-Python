s = input()
d = set()

for i in range(len(s)):
    for j in range(len(s) - i):
        d.add(s[j:j + i + 1])

print(len(d))