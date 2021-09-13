import sys

N = int(input())

lt = [int(x) for x in input().rstrip().split()]

M = int(input())

dp = [[False]*N for _ in range(N)]

for j in range(N):
    for i in range(N):
        if j<i:
            continue
        if i == j:
            dp[i][j] = True
        elif i == j-1:
            if lt[i] == lt[j]:
                dp[i][j] = True
        if i<j-1:
            if dp[i+1][j-1] == True and lt[i] == lt[j]:
                dp[i][j] = True





for i in range(M):
    a,b = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if dp[a-1][b-1]==True:
        print(1)
    else:
        print(0)