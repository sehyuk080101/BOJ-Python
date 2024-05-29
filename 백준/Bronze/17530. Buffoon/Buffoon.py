n = []
for _ in range(int(input())):
    n.append(int(input()))
if max(n) == n[0]:
    print("S")
else:
    print("N")