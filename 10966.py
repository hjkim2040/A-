from collections import deque


def bfs():
    global Sum
    while q:
        y, x = q.popleft()
        diry = [0, 0, 1, -1]
        dirx = [1, -1, 0, 0]
        for i in range(4):
            dy, dx = y + diry[i], x + dirx[i]
            if 0 <= dy < N and 0 <= dx < M and visited[dy][dx] == -1:
                q.append((dy, dx))
                visited[dy][dx] = visited[y][x] + 1
                Sum += visited[dy][dx]


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0
    Sum = 0
    bfs()
    print(f'#{t} {Sum}')