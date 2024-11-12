for _ in range(10):
    num = int(input())
    a = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    vst = [[False for _ in range(102)] for _ in range(100)]
    r, c = 99, a[-1].index(2)
    vst[r][c] = True
    while r > 0:
        if a[r][c - 1] and not vst[r][c - 1]:
            c -= 1
        elif a[r][c + 1] and not vst[r][c + 1]:
            c += 1
        else:
            r -= 1
        vst[r][c] = True
    print(f'#{num} {c - 1}')