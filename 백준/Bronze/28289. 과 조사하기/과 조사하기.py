a = {"sw" : 0, "em" : 0, "ai" : 0, "fs" : 0}
for i in range(int(input())):
    g, c, n = map(int, input().split())
    if g == 1:
        a["fs"] += 1
    elif c == 1 or c == 2:
        a["sw"] += 1
    elif c == 3:
        a["em"] += 1
    else:
        a["ai"] += 1
for i in a:
    print(a[i])