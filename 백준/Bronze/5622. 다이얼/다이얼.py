dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
a = input()
num = 0
for i in range(len(a)):
    for j in range(len(dial)):
        if a[i] in dial[j]:
            num += j + 2
    num += 1
print(num)