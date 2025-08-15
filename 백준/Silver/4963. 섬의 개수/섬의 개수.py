import sys

sys.setrecursionlimit(10 ** 6)


def dfs(a, b, c, d):
    if a < 0 or a >= c or b < 0 or b >= d or m[a][b] == "0":
        return

    m[a][b] = "0"
    dfs(a - 1, b, c, d)
    dfs(a + 1, b, c, d)
    dfs(a, b - 1, c, d)
    dfs(a, b + 1, c, d)
    dfs(a - 1, b - 1, c, d)
    dfs(a - 1, b + 1, c, d)
    dfs(a + 1, b - 1, c, d)
    dfs(a + 1, b + 1, c, d)


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    m = []
    count = 0

    for i in range(h):
        m.append(sys.stdin.readline().split())

    for i in range(h):
        for j in range(w):
            if m[i][j] == "1":
                dfs(i, j, h, w)
                count += 1

    print(count)
