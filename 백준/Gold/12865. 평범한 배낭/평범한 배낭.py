n, k = map(int, input().split())
health = []
happiness = []
happiness_list = [0] * (k + 1)
index_set_list = [set()] * (k + 1)

for i in range(n):
    a, b = map(int, input().split())
    health.append(a)
    happiness.append(b)

for i in range(1, k + 1):
    max_happiness = 0
    index = 0

    for j in range(n):
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

print(max(happiness_list))
