import sys

sys.setrecursionlimit(10 ** 5)

n = int(input())
cnt = 0
l = list(map(int, input().split()))

def qs(li, left, right):
    if left < right:
        pivot = li[left]
        i = left + 1
        j = right
        while i <= j:
            while i <= right and l[i] <= pivot:
                i += 1
            while j >= left and l[j] > pivot:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]
        li[left], li[j] = li[j], li[left]
        qs(li, left, j - 1)
        qs(li, j + 1, right)

qs(l, 0, n - 1)

for k in range(n):
    cnt += l[k] * (n - k)

print(cnt)