while True:
    a, b = map(int, input().split())
    if a + b == 0:
        break
    if not(a % b):
        print("multiple")
    elif not(b % a):
        print("factor")
    else:
        print("neither")