N = int(input())
for i in range(1, N + 1):
    print("*"*i+" "*2*(N - i)+"*"*i)
for k in range(N - 1, 0, -1):
    print("*"*k+" "*2*(N - k)+"*"*k)