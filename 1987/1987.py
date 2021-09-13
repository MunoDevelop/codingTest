import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
g = [[] for _ in range(N)]

def aToIdx(a):
    return ord(a)-ord('A')

for i in range(N):
    g[i] = [aToIdx(x) for x in sys.stdin.readline().rstrip()]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

neighbors = [[[] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        for k in range(4):
            py,px = i + dy[k],j + dx[k]
            if px in range(M) and py in range(N):
                neighbors[i][j].append((py,px))


visited = [[False] * M for N in range(N)]
mx = 0

d = [False]*26
d[g[0][0]] = True
visited[0][0] = True


def dfs(y, x, depth):
    global mx
    if mx == 26:
        return
    mx = max(mx,depth)
    for py,px in neighbors[y][x]:
        v = g[py][px]
        if not visited[py][px] and not d[v]:
            d[v] = True
            visited[py][px] = True
            dfs(py, px,depth+1)
            d[v] = False
            visited[py][px] = False

dfs(0, 0, 1)

print(mx)
