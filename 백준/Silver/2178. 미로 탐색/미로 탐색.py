from collections import deque

graph = {}


def bfs(start_v, n, m):
    discovered = []
    queue = deque([[start_v, 1]])

    while queue:
        v = queue.popleft()
        if v[0] == n * m:
            return v[1]

        if v[0] not in discovered:
            discovered.append(v[0])

            for w in graph[v[0]]:
                queue.append([w, v[1] + 1])

    return None


n, m = map(int, input().split())
l = []

for i in range(n):
    l.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        a = m * i + j + 1
        if l[i][j] == 1:
            graph[a] = []
            if j > 0:
                if l[i][j - 1] == 1:
                    graph[a].append(a - 1)
            if j < m - 1:
                if l[i][j + 1] == 1:
                    graph[a].append(a + 1)
            if i > 0:
                if l[i - 1][j] == 1:
                    graph[a].append(a - m)
            if i < n - 1:
                if l[i + 1][j] == 1:
                    graph[a].append(a + m)

print(bfs(1, n, m))
