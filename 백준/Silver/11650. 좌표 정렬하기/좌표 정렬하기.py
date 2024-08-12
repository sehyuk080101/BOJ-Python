arr = [[] for i in range(200001)]
xcoor = set()

for i in range(int(input())):
    x, y = map(int, input().split())
    arr[x + 100000] += [y]
    xcoor.add(x + 100000)

for i in sorted(xcoor):
    for j in sorted(arr[i]):
        print(i - 100000, j)