calpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
num = 0
i = 0
a = input()
while i < len(a):
    if i < len(a) - 2:
        if a[i] + a[i + 1] + a[i + 2] in calpha:
            i += 2
        elif a[i] + a[i + 1] in calpha:
            i += 1
    elif i < len(a) - 1:
        if a[i] + a[i + 1] in calpha:
            i += 1
    i += 1
    num += 1
print(num)