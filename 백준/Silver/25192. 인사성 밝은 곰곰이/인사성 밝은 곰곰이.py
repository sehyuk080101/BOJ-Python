n = int(input())
cnt = 0

for i in range(n):
    s = input()
    if s == "ENTER":
        d = set()
    else:
        if s not in d:
            cnt += 1
        d.add(s)
        
print(cnt)