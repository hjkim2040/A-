def dfs(n, alst, blst) :
    global ans
    if n == N:
        if len(alst) == M:
            asum = bsum = 0
            for i in range(M) :
                for j in range(M) :
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asum - bsum))
        return
    dfs(n + 1, alst + [n], blst)
    dfs(n + 1, alst, blst + [n])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    M = N // 2
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 20000*N*N
    dfs(0, [], [])
    print(f'#{test_case} {ans}')