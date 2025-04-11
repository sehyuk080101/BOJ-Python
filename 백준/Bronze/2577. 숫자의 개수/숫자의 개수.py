l = [0] * 10

a = int(input())
b = int(input())
c = int(input())

for i in str(a * b * c):
    l[int(i)] += 1

for i in l:
    print(i)