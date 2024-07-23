n, k = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[-k])