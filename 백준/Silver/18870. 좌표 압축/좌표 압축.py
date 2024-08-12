n = int(input())
a = list(map(int, input().split()))
arr = sorted(set(a))
idx = [i for i in range(len(arr))]
d = {}
for i in range(len(arr)):
    d[arr[i]] = idx[i]
for i in a:
    print(d[i], end=" ")