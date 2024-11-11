def dfs(y, x, path, cnt):
    global i, j, result
    if cnt == 3 and y == i and x == j and len(path) > 2:
        result = max(result, len(path))
        return

    if 0 <= y < len(cafe) and 0 <= x < len(cafe[y]) and cafe[y][x] not in path:
        dy, dx = y + diry[cnt], x + dirx[cnt]
        new_path = path + [cafe[y][x]]
        dfs(dy, dx, new_path, cnt)
        if cnt < 3:
            dy, dx = y + diry[cnt + 1], x + dirx[cnt + 1]
            new_path = path + [cafe[y][x]]
            dfs(dy, dx, new_path, cnt + 1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    diry = [1, 1, -1, -1]
    dirx = [1, -1, -1, 1]
    result = -1
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0)
    print(f'#{t} {result}')