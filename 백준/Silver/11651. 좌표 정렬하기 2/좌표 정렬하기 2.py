arr = [[] for i in range(200001)]
ycoor = set()

for i in range(int(input())):
    x, y = map(int, input().split())
    arr[y + 100000] += [x]
    ycoor.add(y + 100000)

for i in sorted(ycoor):
    for j in sorted(arr[i]):
        print(j, i - 100000)