a = int(input())
b = int(input())
t = 0
for i in range(b):
    c, d = map(int, input().split())
    t += c * d
if t == a:
    print("Yes")
else:
    print("No")