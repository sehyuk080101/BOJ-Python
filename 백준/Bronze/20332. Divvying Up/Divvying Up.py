n = input()
w = list(map(int, input().split()))
if sum(w) / 3 % 1 == 0:
    print("yes")
else:
    print("no")