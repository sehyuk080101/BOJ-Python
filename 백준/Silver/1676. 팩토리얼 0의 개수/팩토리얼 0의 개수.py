n = int(input())
f = 1
count = 0

for i in range(1, n + 1):
    f *= i

s = str(f)
j = -1

while s[j] == "0":
    count += 1
    j -= 1

print(count)
