from collections import deque
import sys
d = deque()

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().split()

    if s[0] == "1":
        d.appendleft(s[1])
    elif s[0] == "2":
        d.append(s[1])
    elif s[0] == "3":
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif s[0] == "4":
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif s[0] == "5":
        print(len(d))
    elif s[0] == "6":
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "7":
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    else:
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])