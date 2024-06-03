c = {"Q1" : 0, "Q2" : 0, "Q3" : 0, "Q4" : 0, "AXIS" : 0}
for _ in range(int(input())):
    x, y = map(int, input().split())
    if not(x) or not(y):
        c["AXIS"] += 1
    else:
        if x > 0 and y > 0:
            c["Q1"] += 1
        elif x < 0 and y > 0:
            c["Q2"] += 1
        elif x < 0 and y < 0:
            c["Q3"] += 1
        else:
            c["Q4"] += 1
for k, v in c.items():
    print(f"{k}: {v}")