while True:
    s = input()
    stack = []
    tf = True
    if s == ".":
        break
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if len(stack) == 0:
                print("no")
                tf = False
                break
            if i == ")":
                a = stack.pop()
                if a == "[":
                    print("no")
                    tf = False
                    break
            else:
                a = stack.pop()
                if a == "(":
                    print("no")
                    tf = False
                    break
    if tf:
        if s[-1] == ".":
            if len(stack) == 0:
                print("yes")
            else:
                print("no")
        else:
            print("no")