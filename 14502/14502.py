import sys
from collections import deque

def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next

perm = [(1,0),(-1,0),(0,1),(0,-1)]

N,M = [int(x) for x in sys.stdin.readline().rstrip().split()]
origin = []
visited = [[False]*M for _ in range(N)]
for i in range(N):
    origin.append([int(x) for x in sys.stdin.readline().rstrip().split()])
virus = []
walls = []
for i in range(N):
    for j in range(M):
        if origin[i][j] == 2:
            virus.append((i,j))
        elif origin[i][j] == 0:
            walls.append((i,j))
g = [[0]*M for x in range(N)]

def reset():
    for i in range(N):
        for j in range(M):
            g[i][j] = origin[i][j]
            visited[i][j] = False

reset()

def bfs(start):
    q = deque()
    if visited[start[0]][start[1]]:
        return 0
    q.append(start)
    visited[start[0]][start[1]] = True
    while len(q) != 0:
        vert = q.popleft()
        for neighbor in [(vert[0]+x[0], vert[1]+x[1]) for x in perm]:
            if neighbor[0] not in range(N) or neighbor[1] not in range(M):
                continue
            if g[neighbor[0]][neighbor[1]] == 1 or g[neighbor[0]][neighbor[1]] == 2:
                continue
            if visited[neighbor[0]][neighbor[1]]:
                continue
            q.append(neighbor)
            g[neighbor[0]][neighbor[1]] = 2
            visited[neighbor[0]][neighbor[1]] = True

a = 0
for choice in combinations(walls,3):
    for i in choice:
        g[i[0]][i[1]] = 1

    for v in virus:
        bfs(v)
    cnt = 0
    for i in g:
        for j in i:
            if j == 0:
                cnt += 1
    if cnt > a:
        a = cnt
    reset()
print(a)