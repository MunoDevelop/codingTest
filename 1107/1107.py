import math
def product(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr,r-1):
                yield [arr[i]] + next

TargetNum = int(input())
targetDigits = 0
if TargetNum!=0:
    targetDigits = int(math.log10(TargetNum))+1
else:
    targetDigits = 1
targetDigits+=1
brokenBtnLength = int(input())
lt = []
if brokenBtnLength >0:
    lt =[int(x) for x in input().split()]
valibleBtns = [x for x in range(10) if x not in lt]
mini = 9999999
while targetDigits>0:
    for num in product(valibleBtns,targetDigits):
        fixedNum = "".join([str(i) for i in num])

        k = abs(int(fixedNum)-TargetNum)+targetDigits
        if k<mini:
            mini = k

    targetDigits-=1
print(min(abs(TargetNum-100),mini))
#print(i)
