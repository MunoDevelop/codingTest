import sys
import heapq

n,m,x = [int(x) for x in input().split()]

g = [[]for i in range(n)]
inf = int(1e10)
disList = [inf] * n

inList = []
for i in range(m):
    a, b, l = [int(x) for x in sys.stdin.readline().split()]
    inList.append((a,b,l))

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

for i in range(m):
    a,b,l = inList[i]
    g[a-1].append((b-1,l))
x-=1
stra(x)
tempDisList = disList[:]

g = [[]for i in range(n)]
disList = [inf] * n

for i in range(m):
    a, b, l = inList[i]
    g[b-1].append((a-1,l))
stra(x)
for idx in range(n):
    disList[idx] += tempDisList[idx]

print(max(disList))
