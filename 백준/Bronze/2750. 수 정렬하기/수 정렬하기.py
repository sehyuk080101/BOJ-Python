arr = []

n = int(input())

for i in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(i, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(i)