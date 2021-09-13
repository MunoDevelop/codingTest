import sys
from collections import deque


N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]

g = {}
for i in range(N):
    g[i] = []

degree = [0] * N
result = []
for i in range(M):
    s,e = [int(x) for x in sys.stdin.readline().rstrip().split()]
    g[s-1].append(e-1)
    degree[e-1] += 1

que = deque()
for i in range(N):
    if degree[i] == 0:
        que.append(i)

for _ in range(N):
    if not que:
        #cycle
        break
    present = que.popleft()
    result.append(present+1)
    for i in range(len(g[present])):
        end = g[present][i]
        degree[end]-=1
        if degree[end] == 0:
            que.append(end)
for i in range(len(result)):
    if i == len(result)-1:
        print(f'{result[i]}', end="")
    else:
        print(f'{result[i]} ', end="")
