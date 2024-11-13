from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
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
        # 배열 복사하기
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
            for i in range(h - 1, -1, -1): # 마지막 행에서 첫번째 행까지 역순으로 순회
                if tarr[i][j]: # 현재 위치에 벽돌이 있는 경우
                    tarr[idx][j], tarr[i][j] = tarr[i][j], tarr[idx][j] # 벽돌을 아래로 내림
                    idx -= 1 # 다음 빈 공간으로 이동
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

# 1. 입력받은 정보 초기화
# 2. 방향 배열 초기화
# 3. 총 블록 개수 변수
# 4. 벽돌 배열을 순회하면서 총 블록이 몇 개가 있는지 계산
# 5. dfs, bfs 같이 사용 매개변수( 레벨, 남은 블록 개수, 벽돌 배열)
# 6. 레벨이 n에 도달( 구슬을 쏠 수 있는 횟수 전부 소모), 남은 블록이 없다면 남은 블록의 최소 개수 구하고 리턴
# 7. w번 반복 -> 왼쪽부터 오른쪽 끝까지 구슬을 쐈을 때 나오는 모든 경우의 수를 구하기 위해
# 8. 벽돌 배열을 복사, 위에서 부터 아래로 내려가면서 0이 아닌 부분을 찾았으면 거기서 부터 구슬 쏘기 시작
# 9. deque를 사용 (좌표와 구슬 가중치 추가)
# 10. 총 벽돌 개수 - 1, 해당 좌표 배열을 0으로 바꾸기
# 11. bfs 돌리기 -> 구슬 가중치 만큼 반복 -> 방향 배열을 사용해서 벽돌 깨기
# 12. bfs가 끝나면 깨진 벽돌 부분 채우기 -> 밑에서 부터 올라가면서 현재 위치에 벽돌이 있으면 아래로 내림
# 13. 벽돌 재배치가 끝나면 재귀로 다시 들어가기


