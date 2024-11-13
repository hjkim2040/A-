import sys
sys.stdin = open('input.txt', 'r')

# def dfs(n, alst, blst) :
#     global ans
#     # 식재료 모두 사용시
#     if n == N:
#         # 요리 하나에 식재료 2개 사용시
#         if len(alst) == M:
#             # 식재료 시너지 점수 0으로 초기화
#             asum = bsum = 0
#             for i in range(M) :
#                 for j in range(M) :
#                     asum += arr[alst[i]][alst[j]]
#                     bsum += arr[blst[i]][blst[j]]
#             ans = min(ans, abs(asum - bsum))
#         return
#     dfs(n + 1, alst + [n], blst)
#     dfs(n + 1, alst, blst + [n])
#
# T = int(input())
# for test_case in range(1, T + 1):
#     # N은 식재료 수
#     N = int(input())
#     # M은 식재료를 N / 2개씩 나누어서 요리 하기 위해
#     M = N // 2
#     # 시너지 배열
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = 20000*N*N
#     dfs(0, [], [])
#     print(f'#{test_case} {ans}')

# 1. 입력값 받아서 배열 및 변수 초기화
# 2. 식재료 리스트 절반씩 나눠서 dfs
# 3. level이 식재료 개수 만큼 도달 -> A리스트 길이가 식재료 개수 절반에 도달
# 4. A, B 시너지 합 초기화 -> 모든 조합 순회하면서 맛의 차이가 제일 적은 식재료 조합 찾기

def dfs(level, alist, blist) :
    global result
    if level == N :
        if len(alist) == M :
            asum = bsum = 0
            for i in range(M) :
                for j in range(M) :
                    asum += arr[alist[i]][alist[j]]
                    bsum += arr[blist[i]][blist[j]]
            result = min(result, abs(asum - bsum))
        return
    dfs(level + 1, alist + [level], blist)
    dfs(level + 1, alist, blist + [level])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = N // 2
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 21e8
    dfs(0, [], [])
    print(f'#{tc} {result}')