arr = [[] for i in range(201)]
agearr = set()
for _ in range(int(input())):
    age, name = input().split()
    agearr.add(int(age))
    arr[int(age)].append(name)

for i in sorted(agearr):
    for j in arr[i]:
        print(i, j)