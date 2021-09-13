import sys
from collections import deque


N,M = [int(x) for x in sys.stdin.readline().rstrip().split()]

g = [[] for _ in range(N)]
degree = [0] * N
result = []

nVisitList = []


for i in range(M):
    lt = [int(x) for x in sys.stdin.readline().rstrip().split()]
    for i in range(1,lt[0]):
        a,b = lt[i]-1,lt[i+1]-1

        if b not in  g[a]:
            g[a].append(b)
            #print(f'{a+1} to {b+1}')
            degree[b]+=1

que = deque()

for i in range(N):
    if degree[i] == 0:
        que.append(i)

for i in range(N):
    #if len(que)>1:
        # print("?")
        #break
    if not que:
        print("0")
        break
    present = que.popleft()
    result.append(present+1)
    for i in range(len(g[present])):
        end = g[present][i]
        degree[end]-=1
        if degree[end] == 0:
            que.append(end)
else:
    for i in result:
        print(i)
