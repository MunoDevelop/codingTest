import sys
import math

N, M, T = [int(x) for x in sys.stdin.readline().rstrip().split()]
g = []
for i in range(N):
    g.append([int(x) for x in sys.stdin.readline().rstrip().split()])
aconPosList = []
for i in range(N):
    for j in range(M):
        if g[i][j] == -1:
            aconPosList.append((i,j))


def valid_index(i, j):
    if i in range(N) and j in range(M):
        return True
    else:
        return False


def valid_neighbors(i, j):
    lst = []
    if valid_index(i + 1, j) and g[i + 1][j] != -1:
        lst.append((i + 1, j))
    if valid_index(i - 1, j) and g[i - 1][j] != -1:
        lst.append((i - 1, j))
    if valid_index(i, j + 1) and g[i][j + 1] != -1:
        lst.append((i, j + 1))
    if valid_index(i, j - 1) and g[i][j - 1] != -1:
        lst.append((i, j - 1))
    return lst


def spread(g):
    fixedG = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if g[i][j] <= 0:
                continue
            red = 0
            for k in valid_neighbors(i,j):
                val = g[i][j] // 5
                fixedG[k[0]][k[1]] += val
                red -= val
            fixedG[i][j] += red
    for i in range(N):
        for j in range(M):
            g[i][j] += fixedG[i][j]


def operate(aconPosList):
    fixedG = [[0] * M for _ in range(N)]

    moveRightPosList = []
    moveLeftPosList = []
    moveUpPosList = []
    moveDownPosList = []

    uPosY = aconPosList[0][0]
    dPosY = aconPosList[1][0]

    for j in range(1,M-1):
        moveRightPosList.append((uPosY, j))
        moveRightPosList.append((dPosY, j))

    for j in range(1,M):
        moveLeftPosList.append((0,j))
        moveLeftPosList.append((N-1,j))

    for i in range(1,uPosY+1):
        moveUpPosList.append((i,M-1))
    for i in range(0,uPosY):
        moveDownPosList.append((i,0))

    for i in range(dPosY+1,N):
        moveUpPosList.append((i,0))
    for i in range(dPosY,N-1):
        moveDownPosList.append((i,M-1))

    for pos in moveUpPosList:
        y,x = pos
        fixedG[y-1][x] = g[y][x]
    for pos in moveLeftPosList:
        y, x = pos
        fixedG[y][x-1] = g[y][x]
    for pos in moveRightPosList:
        y, x = pos
        fixedG[y][x+1] = g[y][x]
    for pos in moveDownPosList:
        y,x = pos
        fixedG[y+1][x] = g[y][x]
    fixedG[uPosY][0] = -1
    fixedG[dPosY][0] = -1

    aList = []
    aList += moveRightPosList
    aList += moveLeftPosList
    aList += moveUpPosList
    aList += moveDownPosList

    for i in range(N):
        for j in range(M):
            if (i,j) in aList:
                g[i][j] = fixedG[i][j]
    return 0

for i in range(T):
    spread(g)
    operate(aconPosList)
s = 0
for i in range(N):
    for j in range(M):
        s += g[i][j]
print(s+2)

