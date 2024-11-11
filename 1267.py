def dfs(node, visited, stack):
    visited.add(node)

    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node, visited, stack)

    stack.append(node)


T = 10
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = set()
    stack = []
    graph = [[] for _ in range(V + 1)]

    for i in range(0, 2 * E, 2):
        graph[arr[i]].append(arr[i + 1])

    for v in range(1, V + 1):
        if v not in visited:
            dfs(v, visited, stack)

    print(f"#{tc}", *stack[::-1])