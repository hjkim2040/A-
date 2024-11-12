from collections import deque


def bfs(start, end, max_cut):
    q = deque()
    visited = set()

    q.append((*start, 0, 0, 0))
    visited.add((*start, 0))

    while q:
        y, x, dir, cuts, moves = q.popleft()

        dy, dx = y + diry[dir], x + dirx[dir]
        if 0 <= dy < len(field) and 0 <= dx < len(field[dy]):
            if (dy, dx) == end:
                return moves + 1
            if field[dy][dx] == 'G' and (dy, dx, dir) not in visited:
                visited.add((dy, dx, dir))
                q.append((dy, dx, dir, cuts, moves + 1))
            elif field[dy][dx] == 'T' and cuts < max_cut and (dy, dx, dir) not in visited:
                visited.add((dy, dx, dir))
                q.append((dy, dx, dir, cuts + 1, moves + 1))

        new_dir = (dir - 1) % 4
        if (y, x, new_dir) not in visited:
            visited.add((y, x, new_dir))
            q.append((y, x, new_dir, cuts, moves + 1))

        new_dir = (dir + 1) % 4
        if (y, x, new_dir) not in visited:
            visited.add((y, x, new_dir))
            q.append((y, x, new_dir, cuts, moves + 1))

    return -1


T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    start = 0
    end = 0
    diry = [-1, 0, 1, 0]
    dirx = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start = (i, j)
            elif field[i][j] == 'Y':
                end = (i, j)
    result = bfs(start, end, K)
    print(f'#{t} {result}')