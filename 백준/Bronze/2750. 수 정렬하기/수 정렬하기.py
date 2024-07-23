arr = []

for i in range(int(input())):
    arr.append(int(input()))

while True:
    k = 0

    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
        else:
            k += 1

    if k == len(arr) - 1:
        break

for i in arr:
    print(i)