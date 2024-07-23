n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(i)