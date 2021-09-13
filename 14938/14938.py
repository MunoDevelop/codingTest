import sys
import heapq

n, m, r = [int(x) for x in input().rstrip().split()]

itemsInArea = [int(x) for x in input().rstrip().split()]
g = [[-1]*n for _ in range(n)]
inf = 1000000
disList = [inf] * n  # one dummy

for i in range(r):
    a, b, l = [int(x) for x in input().rstrip().split()]
    g[a-1][b-1] = l
    g[b-1][a-1] = l

itmMaxList = []
def stra(idx):
    hq = []
    disList = [inf] * n
    disList[idx] = 0
    heapq.heappush(hq,(0,idx))
    itm = 0
    while hq:
        current = heapq.heappop(hq)[1]
        for dest,dist in enumerate(g[current]):
            if dist == -1:
                continue
            if disList[current] + dist < disList[dest]:
                disList[dest] = disList[current] + dist
                heapq.heappush(hq,(dist,dest))

    itm = 0
    for i in range(n):
        if disList[i] <= m:
            itm += itemsInArea[i]
    itmMaxList.append(itm)
    #print(disList)
    #print(itm)
for i in range(n):
    stra(i)

print(max(itmMaxList))