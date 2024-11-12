def dfs(i, sm):
    global ans
    if i == N:
        if sm >= B:
            ans = min(ans, sm - B)
        return
    dfs(i + 1, sm + arr[i])
    dfs(i + 1, sm)


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = B
    dfs(0, 0)

    print(f'#{test_case} {ans}')