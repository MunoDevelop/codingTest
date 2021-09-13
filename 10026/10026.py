import sys

N = int(sys.stdin.readline().rstrip())
g = [[''] * N for y in range(N)]
for i in range(N):
    row = [s for s in sys.stdin.readline().rstrip()]
    for j in range(N):
        g[i][j] = row[j]

visited = [[False] * N for y in range(N)]
queue = []
area = 0

def valid_index(i, j):
    if i in range(N) and j in range(N):
        return True
    else:
        return False

def valid_neighbors(i, j, case):
    lst = []
    centerColor = g[i][j]
    validColor = []
    if case == 1:
        validColor.append(centerColor)
    elif case == 2:
        if centerColor == "R" or centerColor == "G":
            validColor.append("R")
            validColor.append("G")
        else:
            validColor.append("B")
    if valid_index(i + 1, j) and not visited[i + 1][j] and g[i + 1][j] in validColor:
        lst.append((i + 1, j))
    if valid_index(i - 1, j) and not visited[i - 1][j] and g[i - 1][j] in validColor:
        lst.append((i - 1, j))
    if valid_index(i, j + 1) and not visited[i][j + 1] and g[i][j + 1] in validColor:
        lst.append((i, j + 1))
    if valid_index(i, j - 1) and not visited[i][j - 1] and g[i][j - 1] in validColor:
        lst.append((i, j - 1))

    return lst


def bfs(i, j, case):
    global area
    if visited[i][j]:
        return 0
    # print('newArea')
    queue.append((i, j))
    visited[i][j] = True
    # print(v+1,end = ' ')
    while len(queue) != 0:
        v = queue.pop(0)
        for k in valid_neighbors(v[0], v[1], case):
            queue.append((k[0], k[1]))
            visited[k[0]][k[1]] = True
            # print(k+1,end = ' ')
    area += 1


# print(g)
for i in range(N):
    for j in range(N):
        bfs(i, j, 1)
print(area,end=" ")
area = 0
visited = [[False] * N for y in range(N)]
queue = []
for i in range(N):
    for j in range(N):
        bfs(i, j, 2)
print(area,end="")