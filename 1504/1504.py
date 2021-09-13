import sys
import heapq

n,r = [int(x) for x in sys.stdin.readline().split()]
#start = int(sys.stdin.readline())-1
g = [[]for i in range(n)]
inf = 100000000
disList = [inf] * n

for i in range(r):
    a, b, l = [int(x) for x in sys.stdin.readline().split()]
    g[a-1].append((b-1,l))
    g[b-1].append((a-1,l))

v1,v2 = [int(x) for x in sys.stdin.readline().split()]

def stra(idx):
    global disList
    hq = []
    disList = [inf] * n
    disList[idx] = 0
    heapq.heappush(hq,(0,idx))
    while hq:
        currentDist,current = heapq.heappop(hq)
        if disList[current] < currentDist:
            continue
        for dest,dist in g[current]:
            if disList[current] + dist < disList[dest]:
                disList[dest] = disList[current] + dist
                heapq.heappush(hq,(dist,dest))
stra(0)
StoV1 = disList[v1-1]
StoV2 = disList[v2-1]
stra(v1-1)
V1toV2 = disList[v2-1]
stra(v2-1)
V2toV1 = disList[v1-1]
caseA = disList[n-1]+StoV1+V1toV2

stra(v1-1)
caseB = disList[n-1]+StoV2+V2toV1

res = min(caseA,caseB)
if res >= inf:
    print(-1)
else:
    print(res)
