import sys

m = int(sys.stdin.readline())
x = set()

for _ in range(m):
    s = sys.stdin.readline().split()

    if s[0] == "add":
        x.add(int(s[1]))
    elif s[0] == "remove":
        if int(s[1]) in x:
            x.remove(int(s[1]))
    elif s[0] == "check":
        if int(s[1]) in x:
            print(1)
        else:
            print(0)
    elif s[0] == "toggle":
        if int(s[1]) in x:
            x.remove(int(s[1]))
        else:
            x.add(int(s[1]))
    elif s[0] == "all":
        for i in range(1, 21):
            x.add(i)
    elif s[0] == "empty":
        x = set()
