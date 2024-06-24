a = sorted(list(map(int, input().split())))

while a[0] + a[1] <= a[2]:
    a[2] -= 1
    
print(sum(a))