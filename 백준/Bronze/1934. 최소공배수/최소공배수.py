for _ in range(int(input())):
    A, B = map(int, input().split())
    for i in range(max(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            print(A * B // i)
            break