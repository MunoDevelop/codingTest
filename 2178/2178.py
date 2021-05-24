import sys


def valid_index(i, j):
    if i in range(N) and j in range(M):
        return True
    else:
        return False


def valid_neighbors(i, j):
    lst = []
    # t,b,l,r
    if valid_index(i+1,j) and not visited[i+1][j] and g[i+1][j] == 1:
        lst.append((i+1,j))
    if valid_index(i-1,j) and not visited[i-1][j] and g[i-1][j] == 1:
        lst.append((i-1,j))
    if valid_index(i,j+1) and not visited[i][j+1] and g[i][j+1] == 1:
        lst.append((i,j+1))
    if valid_index(i,j-1) and not visited[i][j-1] and g[i][j-1] == 1:
        lst.append((i,j-1))
    # lt,rt,lb,rb
    # if valid_index(i-1,j+1) and not visited[i-1][j+1] and g[i-1][j+1] == 1:
    #     lst.append((i-1,j+1))
    # if valid_index(i-1,j-1) and not visited[i-1][j-1] and g[i-1][j-1] == 1:
    #     lst.append((i-1,j-1))
    # if valid_index(i+1,j+1) and not visited[i+1][j+1] and g[i+1][j+1] == 1:
    #     lst.append((i+1,j+1))
    # if valid_index(i+1,j-1) and not visited[i+1][j-1] and g[i+1][j-1] == 1:
    #     lst.append((i+1,j-1))
    return lst


def bfs(i, j):
    if visited[i][j] or g[i][j] == 0:
        return 0
    #print('newArea')

    queue.append((i, j))

    visited[i][j] = True
    #print(v+1,end = ' ')
    while len(queue) != 0:
        v = queue.pop(0)
        for k in valid_neighbors(v[0],v[1]):
            if k[0] == N-1 and k[1] == M-1:
                print(len(find_path(v[0], v[1])))
                #print(len())
                exit()

            queue.append((k[0], k[1]))
            f[k[0]][k[1]][0] = v[0]
            f[k[0]][k[1]][1] = v[1]
            visited[k[0]][k[1]] = True
            #print(k+1,end = ' ')


def find_path(i, j):
    lst = []
    lst.append((N-1,M-1))
    while i != -1 and j != -1:
        lst.append((i, j))
        i,j = f[i][j][0],f[i][j][1]

    return lst


N, M = map(int, input().split())

g = [[0]*M for y in range(N)]
f = [[[-1, -1]for x in range(M)] for y in range(N)]
for i in range(N):
    row = [int(s) for s in input()]
    for j in range(M):
        g[i][j] = int(row[j])

visited = [[False]*M for y in range(N)]
queue = []


#print(g)
#print(f)
bfs(0, 0)
#area.sort()

