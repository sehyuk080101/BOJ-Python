w = input()
res = ""
for i in w:
    if i.isupper():
        res += i.lower()
    else:
        res += i.upper()
print(res)