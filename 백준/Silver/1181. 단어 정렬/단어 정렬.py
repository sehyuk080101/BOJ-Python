arr = [set() for i in range(51)]
lenarr = set()
for _ in range(int(input())):
    word = input()
    lenarr.add(len(word))
    arr[len(word)].add(word)

for i in sorted(lenarr):
    for j in sorted(arr[i]):
        print(j)