s = []
for _ in range(int(input())):
    s.append(int(input()))
if s[2] - s[1] == s[1] - s[0]:
    print(s[-1] + s[1] - s[0])
else:
    print(s[-1] * s[1] // s[0])