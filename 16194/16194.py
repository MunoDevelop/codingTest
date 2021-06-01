M = int(input())
cardList = [int(x) for x in input().split()]

dp = [0]*M

for i in range(len(cardList)):
    if i == 0:
        dp[0] = cardList[0]
    else:
        ma = cardList[i]
        for j in range(i):
            temp = dp[i-1-j]+dp[j]
            if temp < ma:
                ma = temp
        dp[i] = ma
print(dp[-1])


