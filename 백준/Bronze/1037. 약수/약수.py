N = int(input())
A = list(map(int, input().split()))
if len(A) == 1:
    print(A[0] ** 2)
else:
    print(max(A) * min(A))