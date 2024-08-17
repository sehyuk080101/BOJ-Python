n = int(input())
li1 = list(map(int, input().split()))
m = int(input())
li2 = list(map(int, input().split()))
d = {}

for i in li1:
    d[i] = 1

for i in li2:
    if i in d:
        print(1, end=" ")
    else:
        print(0, end=" ")