from collections import deque

# 벽돌 깨기

def shoot(level, nblock, now_arr):
    # 블록 남은 개수
    global ans
    # 기저조건 : 만약 지금 공 n개 쏘면 최소값비교해서 반환하기 ( 총 남은 공이 0개이거나 )
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
        # 벽돌 깨기
        nowblocks = nblock - 1
        # 벽돌 깬 부분은 0으로 처리
        tarr[y][x] = 0

        while q:
            ny, nx, power = q.popleft()
            # 가중치 방향 배열 => 상하좌우로 몇 칸을 없애야 하는지
            for p in range(1, power):
                for d in di:
                    dy, dx = ny + (d[0] * p), nx + (d[1] * p)

                    if 0 <= dy < h and 0 <= dx < w and tarr[dy][dx]:
                        q.append((dy, dx, tarr[dy][dx]))
                        # 벽돌을 깬 부분은 0으로 처리
                        tarr[dy][dx] = 0
                        # 총 벽돌 개수 - 1
                        nowblocks -= 1

        # 사이 사이 빈 부분 밑으로 내려서 채우기
        for j in range(w):
            idx = h - 1
            for i in range(h - 1, -1, -1):
                if tarr[i][j]:
                    tarr[idx][j], tarr[i][j] = tarr[i][j], tarr[idx][j]
                    idx -= 1
        # 다음 공 쏘기
        shoot(level + 1, nowblocks, tarr)


for tc in range(1, 1 + int(input())):
    # n은 구슬 개수, w는 너비, h는 높이
    n, w, h = map(int, input().split())
    # 남은 벽돌 개수
    ans = float('inf')
    # 벽돌 정보 배열
    arr = [list(map(int, input().split())) for _ in range(h)]
    # 방향 배열
    di = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    # 총 블록 개수
    blocks = 0
    # 벽돌 배열을 순회하면서 0이 아닌 곳으면 벽돌 개수 + 1
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                blocks += 1

    shoot(0, blocks, arr)
    print(f'#{tc} {ans}')