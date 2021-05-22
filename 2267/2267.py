N = int(input())
g = [[0]*N for y in range(N)]
for i in range(N):
    row = [s for s in input()]
    for j in range(N):
        g[i][j] = int(row[j])

visited = [[False] *N for y in range(N)]
queue = []
area = []

def valid_index(i,j):
    if i in range(N) and j in range(N):
        return True
    else:
        return False


def valid_neighbors(i, j):
    lst = []
    if valid_index(i+1,j) and not visited[i+1][j] and g[i+1][j] == 1:
        lst.append((i+1,j))
    if valid_index(i-1,j) and not visited[i-1][j] and g[i-1][j] == 1:
        lst.append((i-1,j))
    if valid_index(i,j+1) and not visited[i][j+1] and g[i][j+1] == 1:
        lst.append((i,j+1))
    if valid_index(i,j-1) and not visited[i][j-1] and g[i][j-1] == 1:
        lst.append((i,j-1))
    return lst


def bfs(i,j):
    if visited[i][j] or g[i][j] == 0:
        return 0
    #print('newArea')
    area.append(0)
    queue.append((i, j))
    area[-1] += g[i][j]
    visited[i][j] = True
    #print(v+1,end = ' ')
    while len(queue) != 0:
        v = queue.pop(0)
        for k in valid_neighbors(v[0],v[1]):
            queue.append((k[0], k[1]))
            area[-1] += 1
            visited[k[0]][k[1]] = True
            #print(k+1,end = ' ')

#print(g)
for i in range(N):
    for j in range(N):
        bfs(i, j)
area.sort()
print(len(area))
for i in area:
    print(i)