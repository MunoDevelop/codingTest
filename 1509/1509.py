import sys

lt = [x for x in sys.stdin.readline().rstrip()]
N = len(lt)


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

gdp = [0]*N

def sol():
    for now in range(N):
        if now == 0:
            gdp[now] = 1
        else:
            temp = gdp[now-1]+1
            for i in range(now):
                if dp[i][now]:
                    if i == 0:
                        temp = 1
                    else:
                        temp = min(temp,gdp[i-1]+1)
            gdp[now] = temp

sol()
print(gdp[-1])
# for i in range(N):
#     print(f'{lt[i]} {gdp[i]},',end="")