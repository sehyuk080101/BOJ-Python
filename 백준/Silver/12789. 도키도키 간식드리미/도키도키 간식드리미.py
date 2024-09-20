n = int(input())
l = list(map(int, input().split()))
stack = []
li = []
cnt = 1
tf = True

i = 0
while True:
    if l[i] == cnt:
        li.append(cnt)
        cnt += 1
    elif stack and stack[-1] == cnt:
        li.append(stack.pop())
        i -= 1
        cnt += 1
    else:
        stack.append(l[i])
    if len(stack) >= 2 and stack[-1] > stack[-2]:
        print("Sad")
        tf = False
        break
    i += 1
    if i == n:
        break

if tf:
    if stack:
        if stack[-1] == li[-1] + 1:
            print("Nice")
        else:
            print("Sad")
    else:
        print("Nice")