import sys

arr = list(sys.stdin.readline().strip())

for i in range(len(arr) - 1):
    for j in range(i, len(arr)):
        if int(arr[i]) < int(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    sys.stdout.write(i)