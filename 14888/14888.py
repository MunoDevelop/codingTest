import itertools
import copy
N = int(input())

sequence = [int(x) for x in input().split()]

sourcePool = [int(x) for x in input().split()]

lt = [1,2,3,4]

permuResultList = list(itertools.product(lt,repeat = N-1))

iMax = -1000000000
iMin = 1000000000

for permuList in permuResultList:
    if permuList.count(1)==sourcePool[0] \
        and permuList.count(2)==sourcePool[1] \
        and permuList.count(3)==sourcePool[2] \
        and permuList.count(4)==sourcePool[3] :
        nsequence = copy.deepcopy(sequence)
        for i in range(N-1):
            operator =  permuList[i]
            if operator == 1:
                nsequence[i+1] = nsequence[i]+nsequence[i+1]
            elif operator == 2:
                nsequence[i+1] = nsequence[i]-nsequence[i+1]
            elif operator == 3:
                nsequence[i+1] = nsequence[i]*nsequence[i+1]
            elif operator == 4:
                nsequence[i+1] = int(nsequence[i]/nsequence[i+1])
        result = nsequence[-1]
        if result >iMax:
            iMax = result
        if result <iMin:
            iMin = result
print(iMax)
print(iMin)