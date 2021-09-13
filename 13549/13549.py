import sys
import heapq

inf = 1000000000
start, dest = [int(x) for x in sys.stdin.readline().rstrip().split()]
hq = []
disList = [inf] * 100001

heapq.heappush(hq,(0,start))
disList[start] = 0
while hq:
    current = heapq.heappop(hq)[1]
    # if current == dest:
    #     print(disList[current])
    #     break
    for node in [(0,current*2),(1,current-1),(1,current+1)]:
        if node[1] not in range(100001):
            continue
        if node[0]+disList[current] < disList[node[1]]:
            disList[node[1]] = node[0]+disList[current]
            #print(f'{node[1]} updated{disList[node[1]]}')
            heapq.heappush(hq,node)

print(disList[dest])