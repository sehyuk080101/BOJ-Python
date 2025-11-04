n = int(input())
health = list(map(int, input().split()))
happiness = list(map(int, input().split()))
happiness_list = [0] * 100
index_set_list = [set()] * 100
amount = 0

for i in range(n):
    if health[i] == 0:
        amount += happiness[i]

for i in range(1, 100):
    max_happiness = 0
    index = 0

    for j in range(n):
        if health[j] == 0:
            continue
        if health[j] > i:
            continue
        if j in index_set_list[i - health[j]]:
            continue
        if happiness[j] + happiness_list[i - health[j]] > max_happiness:
            max_happiness = happiness[j] + happiness_list[i - health[j]]
            sub_health = health[j]
            index = j

    happiness_list[i] = max_happiness
    index_set_list[i] = index_set_list[i - health[index]].copy()
    index_set_list[i].add(index)

print(max(happiness_list) + amount)
