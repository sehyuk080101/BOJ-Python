n = int(input())
middle = "666"

for i in range(n - 1):
    while True:
        middle = str(int(middle) + 1)
        if "666" in middle:
            break

print(middle)