a, b, c = map(int, input().split())
if a == b == c:
    print(10000+a*1000)
elif (a == b and b != c):
    if a > c:
        print(1000+max(a, c)*100)
    else:
        print(1000+min(a, c)*100)
elif (b == c and c != a):
    if b > a:
        print(1000+max(b, a)*100)
    else:
        print(1000+min(b, a)*100)
elif (c == a and a != b):
    if c > b:
        print(1000+max(c, b)*100)
    else:
        print(1000+min(c, b)*100)
else: print(max(a, b, c)*100)