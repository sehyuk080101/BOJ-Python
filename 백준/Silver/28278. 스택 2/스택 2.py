import sys

stack = []
n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "1":
        stack.append(s[1])
    elif s[0] == "2":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif s[0] == "3":
        print(len(stack))
    elif s[0] == "4":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
        