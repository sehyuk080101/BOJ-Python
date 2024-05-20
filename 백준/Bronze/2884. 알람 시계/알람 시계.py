a, b = map(int, input().split())
if b - 45 < 0:
    a -= 1
    if  a < 0:
        a = 23
    b = 60 + b - 45
else:
    b -= 45 
print(a, b)