import sys

N = int(sys.stdin.readline().rstrip())
g = []
for i in range(N):
    g.append([int(x) for x in sys.stdin.readline().rstrip().split()])
startPos = (0,0)
for i in range(N):
    for j in range(N):
        if g[i][j] == 9:
            startPos = (i,j)
            g[i][j] = 0
fishStat = 2
eat = 0
time = 0
visited = [[False] * N for _ in range(N)]
pathG = [[(-1,-1) for _ in range(N)] for _ in range(N)]

def valid_index(i, j):
    if i in range(N) and j in range(N):
        return True
    else:
        return False


def valid_neighbors(i, j):
    lst = []
    # t,b,l,r
    if valid_index(i+1,j) and not visited[i+1][j] and g[i+1][j] <= fishStat:
        lst.append((i+1,j))
    if valid_index(i-1,j) and not visited[i-1][j] and g[i-1][j] <= fishStat:
        lst.append((i-1,j))
    if valid_index(i,j+1) and not visited[i][j+1] and g[i][j+1] <= fishStat:
        lst.append((i,j+1))
    if valid_index(i,j-1) and not visited[i][j-1] and g[i][j-1] <= fishStat:
        lst.append((i,j-1))
    return lst


def bfs(i, j):
    if visited[i][j]:
        return 0
    queue = [(i, j)]

    visited[i][j] = True
    validFoodList = []
    while len(queue) != 0:
        v = queue.pop(0)

        for k in valid_neighbors(v[0], v[1]):
            queue.append(k)
            visited[k[0]][k[1]] = True
            pathG[k[0]][k[1]] = (v[0],v[1])
            if 0 < g[k[0]][k[1]] < fishStat:
                lWay = len(findPath((i,j),k))-1
                validFoodList.append((lWay, k))

    if len(validFoodList) == 0:
        return (-1,(-1,-1))
    else:
        m = validFoodList[0][0]
        lt = [x for x in validFoodList if x[0] == m]
        lt.sort(key=lambda ele: (ele[1][0],ele[1][1]))
        return lt[0]


def findPath(start,dest):
    way = []
    while pathG[dest[0]][dest[1]][0] != -1:
        way.append(pathG[dest[0]][dest[1]])
        dest = pathG[dest[0]][dest[1]]
    way.append(start)
    return way


while True:
    res = bfs(startPos[0],startPos[1])
    if res[0] == -1:
        print(time)
        break
    else:
        if res[0]!= -1:
            g[res[1][0]][res[1][1]] = 0
            startPos = (res[1][0],res[1][1])
            time += res[0]
            eat+=1
            if eat == fishStat:
                eat = 0
                fishStat+=1
            visited = [[False] * N for _ in range(N)]
            pathG = [[(-1, -1) for _ in range(N)] for _ in range(N)]
#print(g)
