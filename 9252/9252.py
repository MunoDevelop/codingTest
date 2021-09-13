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

i,j = len(aLt),len(bLt)
lt = []
while dp[i][j] > 0:
    v = dp[i][j]
    if dp[i-1][j] == v:
        i = i-1
        continue
    elif dp[i][j-1] == v:
        j = j-1
        continue
    else:
        lt.append(aLt[i-1])
        i = i-1
        j = j-1
if lt:
    print(''.join(reversed(lt)))