s = int(input())
w = input()
e = 0
for i in w:
    if i == "e":
        e += 1
if e > s - e:
    print("e")
elif e < s - e:
    print(2)
else:
    print("yee")