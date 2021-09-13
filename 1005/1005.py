import sys
from collections import deque

cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    N,M = [int(x) for x in sys.stdin.readline().rstrip().split()]
    g = [[] for _ in range(N)]
    degree = [0] * N
    result = []
    costList = [int(x) for x in sys.stdin.readline().rstrip().split()]
    for i in range(M):
        s,e = [int(x) for x in sys.stdin.readline().rstrip().split()]
        g[s-1].append(e-1)
        degree[e-1]+=1
    que = deque()
    W = int(sys.stdin.readline().rstrip())
    dp = [0] * N
    for i in range(N):
        if degree[i] == 0:
            que.append(i)
            dp[i] = costList[i]
    for i in range(N):
        # if len(que)>1:
        #     print("?")
        #     break
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
            dp[end] = max(dp[end],dp[present]+costList[end])
    # else:
    #     for i in range(len(result)):
    #         if i == len(result)-1:
    #             print(f'{result[i]}')
    #         else:
    #             print(f'{result[i]} ', end="")
    print(dp[W-1])