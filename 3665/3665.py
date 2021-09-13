import sys
from collections import deque

cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    N = int(sys.stdin.readline().rstrip())
    lastYearList = [int(x) for x in sys.stdin.readline().rstrip().split()]
    M = int(sys.stdin.readline().rstrip())

    g = [[] for _ in range(N)]
    degree = [0] * N
    result = []
    for i in range(N):
        for j in range(i+1,N):
            g[lastYearList[i]-1].append(lastYearList[j]-1)
            degree[lastYearList[j]-1]+=1

    for i in range(M):
        s,e = [int(x) for x in sys.stdin.readline().rstrip().split()]
        if lastYearList.index(s)>lastYearList.index(e):
            s, e = s, e
        else:
            s, e = e, s
        g[e-1].remove(s-1)
        degree[s-1]-=1
        g[s-1].append(e-1)
        degree[e-1]+=1
    que = deque()

    for i in range(N):
        if degree[i] == 0:
            que.append(i)
    for i in range(N):
        if len(que)>1:
            print("?")
            break
        if not que:
            print("IMPOSSIBLE")
            break
        present = que.popleft()
        result.append(present+1)
        for i in range(len(g[present])):
            end = g[present][i]
            degree[end]-=1
            if degree[end] == 0:
                que.append(end)
    else:
        for i in range(len(result)):
            if i == len(result)-1:
                print(f'{result[i]}')
            else:
                print(f'{result[i]} ', end="")
