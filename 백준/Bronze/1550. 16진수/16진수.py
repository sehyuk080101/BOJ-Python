j = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}
res = 0
n = input()
for i in range(len(n)):
    if n[i] in j:
        res += j[n[i]] * (16 ** (len(n) - (i + 1)))
    else:
        res += int(n[i]) * (16 ** (len(n) - (i + 1)))
print(res)