N = int(input())
C = map(int, input().split())
s = 0
for i in C:
    if i > N:
        s += N
    else:
        s += i
print(s)