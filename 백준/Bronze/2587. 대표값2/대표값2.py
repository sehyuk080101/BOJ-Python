arr = []
avg = 0

for i in range(5):
    arr.append(int(input()))

for i in arr:
    avg += i

avg //= 5

print(avg)

for i in range(5):
    for j in range(i, 5):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[2])