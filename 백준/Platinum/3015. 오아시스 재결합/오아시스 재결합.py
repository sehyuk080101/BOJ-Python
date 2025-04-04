import sys

l = []
stack = []
n = int(sys.stdin.readline())
cnt = n - 1
d = {}

for i in range(n):
    l.append(int(sys.stdin.readline()))

for i in range(n):
    if stack and l[i] >= l[stack[-1]]:
        cnt -= 1
    while stack and l[i] >= l[stack[-1]]:
        c = l[i]
        if c == l[stack[-1]]:
            if c in d:
                cnt += d[c]
                if len(stack) != d[c]:
                    cnt += 1
                break
        else:
            e = stack.pop()
            if l[e] in d:
                d[l[e]] -= 1

        cnt += 1

        if not stack:
            break

    if stack and stack[-1] != i - 1 and l[stack[-1]] != l[i]:
        cnt += 1

    stack.append(i)
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1

print(cnt)
