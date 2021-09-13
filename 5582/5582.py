import sys

aLt = str(sys.stdin.readline().rstrip())
bLt = str(sys.stdin.readline().rstrip())

dp = [[0] * (len(bLt)+1) for _ in range(len(aLt)+1)]


def lcs(i, j):
    if aLt[i] != bLt[j]:
        dp[i+1][j+1] = 0
        return 0
    elif aLt[i] == bLt[j]:
        dp[i+1][j+1] = dp[i][j] + 1
        return dp[i+1][j+1]


ans = 0
for i in range(len(aLt)):
    for j in range(len(bLt)):
        ans = max(ans,lcs(i, j))

print(ans)
