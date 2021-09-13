import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
g = []
for i in range(N):
    g.append([int(x) for x in sys.stdin.readline().rstrip().split()])

perm = [((0, 1), (0, 2), (0, 3)), ((1, 0), (2, 0), (3, 0))  # 1
    , ((1, 0), (0, 1), (1, 1))  # 2
    , ((1, 0), (0, 1), (0, 2)), ((0, 1), (1, 1), (2, 1)), ((1, 0), (2, 0), (2, 1)), ((1, 0), (1, -1), (1, -2))  # 3
    , ((1, 0), (1, 1), (1, 2)), ((0, 1), (1, 0), (2, 0)), ((0, 1), (0, 2), (1, 2)), ((1, 0), (2, 0), (2, -1))  # 3
    , ((0, 1), (1, 0), (1, -1)), ((0, -1), (1, 0), (1, 1)), ((1, 0), (1, 1), (2, 1)), ((1, 0), (1, -1), (2, -1))  # 4
    , ((2, 0), (1, 0), (1, 1)), ((1, 0), (1, -1), (1, 1)), ((1, 0), (0, 1), (0, -1)), ((-1, 0), (1, 0), (0, -1))]  # 5
res = []
for i in range(N):
    for j in range(M):
        for posList in perm:
            s = 0
            for pos in posList:
                x, y = j + pos[0], i + pos[1]
                if y in range(N) and x in range(M):
                    s += g[y][x]
                else:
                    break
            else:
                s += g[i][j]
                res.append(s)
print(max(res))
