import sys

cnt = 0
nbr = 0

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

def merge(arr, left, mid, right):
    global cnt
    global nbr
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for z in range(left, right + 1):
        arr[z] = temp[z - left]
        cnt += 1
        if cnt == k:
            nbr = arr[z]

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

merge_sort(a, 0, len(a) - 1)

if nbr == 0:
    print(-1)
else:
    print(nbr)