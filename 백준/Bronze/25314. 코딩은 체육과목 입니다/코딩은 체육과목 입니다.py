a = int(input())
b = 0
for i in range(int(a / 4)):
    b += 1
if a % 4 > 0:
    b += 1
print("long "*b+"int")