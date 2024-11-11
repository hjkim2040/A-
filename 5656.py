from collections import deque

# 벽돌 깨기

def shoot(level, nblock, now_arr):
    # 블록 남은 개수
    global ans
    # 기저조건 : 만약 지금 공 n개 쏘면 최소값비교해서 반환하기
    if level == n or not nblock:
        ans = min(ans, nblock)
        return

    # 구현하기
    for x in range(w):
        tarr = [row[:] for row in now_arr]
        for y in range(h):
            if tarr[y][x]:
                break
        else:
            continue

        q = deque()
        q.append((y, x, tarr[y][x]))
        nowblocks = nblock - 1
        tarr[y][x] = 0

        while q:
            ny, nx, power = q.popleft()

            for p in range(1, power):
                for d in di:
                    dy, dx = ny + (d[0] * p), nx + (d[1] * p)

                    if 0 <= dy < h and 0 <= dx < w and tarr[dy][dx]:
                        q.append((dy, dx, tarr[dy][dx]))
                        tarr[dy][dx] = 0
                        nowblocks -= 1

        for j in range(w):
            idx = h - 1
            for i in range(h - 1, -1, -1):
                if tarr[i][j]:
                    tarr[idx][j], tarr[i][j] = tarr[i][j], tarr[idx][j]
                    idx -= 1

        shoot(level + 1, nowblocks, tarr)


for tc in range(1, 1 + int(input())):
    n, w, h = map(int, input().split())
    ans = float('inf')
    arr = [list(map(int, input().split())) for _ in range(h)]
    di = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    blocks = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                blocks += 1

    shoot(0, blocks, arr)
    print(f'#{tc} {ans}')