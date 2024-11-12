import sys
sys.stdin = open('input.txt', 'r')
def dfs(node, visited, stack):
    # 방문 체크
    visited.add(node)
    # 그래프와 연결 되어 있는 요소 탐색
    for next_node in graph[node]:
        # 방문한 적이 없으면
        if next_node not in visited:
            # dfs 탐색
            dfs(next_node, visited, stack)
    # 끝까지 탐색 후 작업 순서 배열에 추가
    stack.append(node)


T = 10
for tc in range(1, T + 1):
    # V는 정점의 개수, E는 간선의 개수
    V, E = map(int, input().split())
    # arr은 간선
    arr = list(map(int, input().split()))
    # 방문 배열
    visited = set()
    # 작업 순서 배열
    stack = []
    # 그래프
    graph = [[] for _ in range(V + 1)]
    # 그래프 초기화
    for i in range(0, 2 * E, 2):
        graph[arr[i]].append(arr[i + 1])
    # 정점이 1부터
    for v in range(1, V + 1):
        # 방문한 적이 없으면
        if v not in visited:
            dfs(v, visited, stack)
    # 작업 순서 배열 거꾸로 출력
    print(f"#{tc}", *stack[::-1])

# 1. 그래프 초기화 => 단방향 그래프
# 2. 방문 배열 초기화
# 3. 작업 순서 배열 초기화
# 4. 입력 받은 값으로 그래프 구현
# 5. 1부터 마지막 노드까지 돌면서 dfs 탐색 => 방문 배열에 없는 경우
# 6. dfs -> 방문 배열에 추가, 만약 그래프와 연결된 노드가 있다면 탐색, 그 노드가 방문 하지 않았다면 dfs 탐색
# 7. 끝까지 탐색 후 작업 순서 배열에 추가




