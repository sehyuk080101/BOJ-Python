top = -1
stack = [0] * 100000
n = int(input())

for i in range(n):
    a = input().split()
    if a[0] == "push":
        top += 1
        stack[top] = a[1]
    elif a[0] == "pop":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif a[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    elif a[0] == "size":
        print(top + 1)
    else:
        if top == -1:
            print(-1)
        else:
            print(stack[top])