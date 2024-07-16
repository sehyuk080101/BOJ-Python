a, b = map(int, input().split())
c = int(input())
d = int(input())
for i in range(d, 101):
    res = a * i + b <= c * i
    if res == False:
        break
if res:
    print(1)
else:
    print(0)