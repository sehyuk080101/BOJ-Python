l = []
n = int(input())

for i in range(n):
    a = int(input())
    if a == 0:
        l.pop()
    else:
        l.append(a)
        
print(sum(l))