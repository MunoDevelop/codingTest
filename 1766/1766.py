import sys
import heapq


N,M = [int(x) for x in sys.stdin.readline().rstrip().split()]
g = [[] for _ in range(N)]
degree = [0] * N
result = []

# lt = list(range(N))
# for i in range(N-1):
#     g[i].append(i+1)
#     degree[i+1] += 1

for i in range(M):
    s,e = [int(x) for x in sys.stdin.readline().rstrip().split()]
    # if e-1 not in g[s-1] and s>e:
    g[s-1].append(e-1)
    degree[e-1]+=1
    # degree[s-1]-=1
# print(degree)
que = []

for i in range(N):
    if degree[i] == 0:
        heapq.heappush(que,i)


for i in range(N):
    # if len(que)>1:
    #     print("?")
    #     break
    if not que:
        print("IMPOSSIBLE")
        break
    present = heapq.heappop(que)
    result.append(present+1)
    for i in range(len(g[present])):
        end = g[present][i]
        degree[end]-=1
        if degree[end] == 0:
            heapq.heappush(que,end)

else:
    for i in range(len(result)):
        if i == len(result)-1:
            print(f'{result[i]}')
        else:
            print(f'{result[i]} ', end="")
