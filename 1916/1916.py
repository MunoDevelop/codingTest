import sys
import heapq

n = int(input())
r = int(input())

g = [[]for i in range(n)]
inf = int(1e10)
disList = [inf] * n

for i in range(r):
    a, b, l = [int(x) for x in sys.stdin.readline().split()]
    g[a-1].append((b-1,l))

def stra(idx):
    hq = []
    disList[idx] = 0
    heapq.heappush(hq,(0,idx))
    while hq:
        currentDist,current = heapq.heappop(hq)
        if disList[current] < currentDist:
            continue
        for dest,dist in g[current]:
            if disList[current] + dist < disList[dest]:
                disList[dest] = disList[current] + dist
                heapq.heappush(hq,(disList[dest],dest))

start,end = [int(x)-1 for x in input().split()]

stra(start)
print(disList[end])
