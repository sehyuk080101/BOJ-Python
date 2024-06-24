while True:
    n = int(input())
    d = []
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            d.append(i)
    if sum(d) == n:
        print(n, "=", end = " ")
        for i in range(len(d)):
            if i == len(d) - 1:
                print(d[i])
                break
            print(d[i], "+", end = " ")
    else:
        print(n, "is NOT perfect.")