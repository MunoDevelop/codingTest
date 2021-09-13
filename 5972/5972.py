import sys
import heapq

n,r = [int(x) for x in input().split()]


g = [[]for i in range(n)]
inf = int(1e10)
disList = [inf] * n

for i in range(r):
    a, b, l = [int(x) for x in sys.stdin.readline().split()]
    g[a-1].append((b-1, l))
    g[b-1].append((a-1,l))


def stra(idx):
    hq = []
    disList[idx] = 0
    heapq.heappush(hq,(0,idx))
    destList = []
    while hq:
        currentDist,current = heapq.heappop(hq)
        if disList[current] < currentDist:
            continue
        for dest,dist in g[current]:
            if disList[current] + dist < disList[dest]:
                disList[dest] = disList[current] + dist
                heapq.heappush(hq,(disList[dest],dest))
                destList.append(dest)
    return destList

start,end = [0,n-1]
stra(start)

print(disList[end])
