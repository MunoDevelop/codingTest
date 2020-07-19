import itertools

N = int(input())

lt = [int(x) for x in list(input().split(" "))]
permuList = list(itertools.permutations(lt,N))
result = 0
for i in range(len(permuList)):
    sum = 0
    for j in range(len(permuList[i])-1):
        sum+=abs(permuList[i][j]-permuList[i][j+1])
    if result==0:
        result = sum
    elif result < sum:
        result = sum

print(result)
