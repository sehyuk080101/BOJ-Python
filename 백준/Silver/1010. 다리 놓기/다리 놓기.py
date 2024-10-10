import math

for i in range(int(input())):
    k, n = map(int, input().split())

    print(math.factorial(n) // math.factorial(n - k) // math.factorial(k))