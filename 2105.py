import sys
sys.stdin = open('input.txt', 'r')
def dfs(y, x, path, cnt):
    global i, j, result
    # 3번 방향을 바꾸고 제자리로 돌아왔고 방문한 디저트 카페 수가 3 이상이면
    if cnt == 3 and y == i and x == j and len(path) > 2:
        # 결과 업데이트 => 더 많은 디저트 투어 경로로
        result = max(result, len(path))
        return

    # 지역을 넘으면 안된다 그리고 같은 메뉴를 파는 디저트 카페도 제외
    if 0 <= y < len(cafe) and 0 <= x < len(cafe[y]) and cafe[y][x] not in path:
        # 지역의 끝에 도달하기 전까지 직진 => 같은 방향으로 계속 가기
        dy, dx = y + diry[cnt], x + dirx[cnt]
        # 방문한 디저트 카페 경로 추가
        new_path = path + [cafe[y][x]]
        # 다시 탐색
        dfs(dy, dx, new_path, cnt)
        # 끝까지 갔는데 방향을 3번 미만으로 바꿨다면 방향 전환
        if cnt < 3:
            dy, dx = y + diry[cnt + 1], x + dirx[cnt + 1]
            new_path = path + [cafe[y][x]]
            # 방향 전환을 했기 때문에 cnt + 1
            dfs(dy, dx, new_path, cnt + 1)

T = int(input())
for t in range(1, T + 1):
    # 지역의 한 변의 길이
    N = int(input())
    # 디저트의 종류
    cafe = [list(map(int, input().split())) for _ in range(N)]
    # 방향 배열
    diry = [1, 1, -1, -1]
    dirx = [1, -1, -1, 1]
    # 결과 변수
    result = -1
    # 모든 디저트 카페를 전부 순회
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0)
    print(f'#{t} {result}')

# 1. 디저트 카페 배열 초기화
# 2. 방향 배열 초기화
# 3. 결과 변수 초기화
# 4. 모든 디저트 카페 순회
# 5. dfs -> 리턴 조건 : 방향 3번 바꾸기, 원래 자리로 돌아가기, 방문한 카페 3곳 이상 -> 결과 변수 업데이트
# 6. 지역을 벗어나면 안된다. 방문한 곳도 패스
# 7. 방향은 직진 -> 지역을 벗어났을 경우 방향 전환 ( 방향 전환을 3번 미만으로 했을 때만 가능 )
# 8. 방문한 곳 배열 추가

