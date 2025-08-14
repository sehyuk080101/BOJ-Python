s = input()
n = 0
a = ""
i = 0

while i < len(s):
    if s[i] == "-":
        if a != "":
            n += sum(map(int, a.split("+")))

        a = ""
        b = i

        for j in range(b + 1, len(s)):
            if s[j] == "-":
                break

            a += s[j]
            i += 1

        l = map(int, a.split("+"))
        n -= sum(l)
        a = ""
        i += 1
    else:
        a += s[i]
        i += 1

if a != "":
    n += sum(map(int, a.split("+")))

print(n)
