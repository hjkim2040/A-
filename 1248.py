T = int(input())
for tc in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    chr = [[] for _ in range(V + 1)]
    par = [0] * (V + 1)

    check = [0] * (V + 1)  # n1 조상노드 표시

    for i in range(E):
        t1, t2 = arr[i * 2], arr[i * 2 + 1]
        chr[t1].append(t2)
        par[t2] = t1

    # n1 조상 찾기
    p = n1
    while p != 0:
        check[p] = 1
        p = par[p]

    # n2 조상 중 n1 조상 찾기
    p = n2
    while check[p] == 0:
        p = par[p]

    q = [p]
    cnt = 0
    while q:
        t = q.pop(0)
        cnt += 1
        for w in chr[t]:
            q.append(w)

    print(f'#{tc} {p} {cnt}')