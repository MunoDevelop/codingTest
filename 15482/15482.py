import sys

aLt = str(sys.stdin.readline().rstrip())
bLt = str(sys.stdin.readline().rstrip())

dp = [[0] * (len(bLt)+1) for _ in range(len(aLt)+1)]


def lcs(i, j):
    if aLt[i] != bLt[j]:
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return 0
    elif aLt[i] == bLt[j]:
        dp[i+1][j+1] = dp[i][j]+1
        return 0


ans = 0
for i in range(len(aLt)):
    for j in range(len(bLt)):
        lcs(i, j)

print(dp[len(aLt)][len(bLt)])
