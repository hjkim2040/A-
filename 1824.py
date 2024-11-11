from collections import deque

# 오 아래 왼 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())

for tc in range(1, t + 1):
    q = deque([(0, 0, 0, 0)])
    n, m = map(int, input().split())
    board = [list(map(str, input())) for _ in range(n)]

    vis = [[[[False] * 16 for _ in range(4)] for _ in range(m)] for _ in range(n)]

    while q:
        # print(q)
        x, y, dir, cnt = q.popleft()
        mapper = board[x][y]

        if mapper == "@":
            print("#{} {}".format(tc, "YES"))
            break

        elif mapper == "^":
            dir = 3

        elif mapper == "v":
            dir = 1

        elif mapper == ">":
            dir = 0

        elif mapper == "<":
            dir = 2

        elif mapper == "_":
            dir = 0 if cnt == 0 else 2

        elif mapper == "|":
            dir = 1 if cnt == 0 else 3

        elif mapper == "?":
            for i in range(4):
                nx = (x + dx[i]) % n
                ny = (y + dy[i]) % m
                if not vis[nx][ny][i][cnt]:
                    q.append((nx, ny, i, cnt))
                    vis[nx][ny][i][cnt] = True

        elif mapper.isdigit():
            cnt = int(mapper)

        elif mapper == "-":
            if cnt == 0:
                cnt = 15
            else:
                cnt -= 1

        elif mapper == "+":
            if cnt == 15:
                cnt = 0
            else:
                cnt += 1

        nx = (x + dx[dir]) % n
        ny = (y + dy[dir]) % m

        if not vis[nx][ny][dir][cnt]:
            q.append((nx, ny, dir, cnt))
            vis[nx][ny][dir][cnt] = True

    else:
        print("#{} {}".format(tc, "NO"))