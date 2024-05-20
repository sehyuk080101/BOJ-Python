num = {}
res = 0
ch = ""
N, B = input().split()
B = int(B)
if B >= 10:
    for i in range(B - 10):
        num[chr(i + 65)] = i + 10
for i in range(len(N)):
    if 65 <= ord(N[i]) <= 90:
        res += num[N[i]] * B ** (len(N) - (i + 1))
    else:
        ch = N[i]
        ch = int(ch)
        res += ch * B ** (len(N) - (i + 1))
print(res)