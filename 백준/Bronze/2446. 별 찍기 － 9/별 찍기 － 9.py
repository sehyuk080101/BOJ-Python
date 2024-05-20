N = int(input())
for i in range(N):
    print(" "*i+"*"*(2*(N - i) - 1))
for k in range(N - 2, -1, -1):
    print(" "*k+"*"*(2*(N - k) - 1))