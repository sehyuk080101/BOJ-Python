from collections import deque


def dfs(v, discovered=None):
    if discovered is None:
        discovered = []

    discovered.append(v)

    for w in d[v]:
        if w not in discovered:
            discovered = dfs(w, discovered)

    return discovered


def bfs(v):
    discovered = []
    queue = deque([v])

    while queue:
        c = queue.popleft()

        if c not in discovered:
            discovered.append(c)

            for w in d[c]:
                queue.append(w)

    return discovered


n, m, v = map(int, input().split())

d = {}

for i in range(m):
    a, b = map(int, input().split())

    if a not in d:
        d[a] = [b]
    else:
        d[a].append(b)

    if b not in d:
        d[b] = [a]
    else:
        d[b].append(a)

for i in d:
    d[i] = sorted(d[i])

for i in range(1, n + 1):
    if i not in d:
        d[i] = []

print(*dfs(v))
print(*bfs(v))
