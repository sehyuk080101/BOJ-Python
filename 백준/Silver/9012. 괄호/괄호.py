n = int(input())

for i in range(n):
    stack = []
    a = input()
    tf = True
    for j in a:
        if j == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                print("NO")
                tf = False
                break
            else:
                stack.pop()
    if tf:
        if stack:
            print("NO")
        else:
            print("YES")