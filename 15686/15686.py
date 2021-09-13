import sys


def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

N,M = [int(x) for x in sys.stdin.readline().rstrip().split()]
g = []

for i in range(N):
    g.append([int(x) for x in sys.stdin.readline().rstrip().split()])
chickens = []
house = []
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            house.append((i,j))
        elif g[i][j] == 2:
            chickens.append((i,j))
lt = []
for rest in combinations(chickens,M):
    s = 0
    for i in range(len(house)):
        s += min([dist(house[i],x) for x in rest])
    lt.append(s)
print(min(lt))