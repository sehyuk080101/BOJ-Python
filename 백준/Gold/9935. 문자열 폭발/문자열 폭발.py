s = input()
e = input()

stack = []
for i in s:
    stack.append(i)
    if i == e[-1] and len(stack) >= len(e):
        a = ""
        for j in range(1, len(e) + 1):
            a = stack[-j] + a
        if a == e:
            for j in range(len(e)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    for i in stack:
        print(i, end="")