import sys


def merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if len(arr[i]) > len(arr[j]):
            temp.append(arr[i])
            i += 1
        elif len(arr[i]) < len(arr[j]):
            temp.append(arr[j])
            j += 1
        else:
            for _ in range(min(len(arr[i]), len(arr[j]))):
                if ord(arr[i][_]) < ord(arr[j][_]):
                    temp.append(arr[i])
                    i += 1
                    break
                elif ord(arr[i][_]) > ord(arr[j][_]):
                    temp.append(arr[j])
                    j += 1
                    break

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for a in range(left, right + 1):
        arr[a] = temp[a - left]


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

d1 = {}
n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if len(s) >= m:
        if s in d1:
            d1[s] += 1
        else:
            d1[s] = 1

d2 = {}

for k, v in d1.items():
    if v in d2:
        d2[v].append(k)
    else:
        d2[v] = [k]

d3 = sorted(d2.items(), key=lambda x: x[0], reverse=True)

for k in d3:
    merge_sort(k[1], 0, len(k[1]) - 1)
    for z in k[1]:
        print(z)