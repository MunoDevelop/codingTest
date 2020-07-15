import itertools

def GCD(a,b):
    if(b==0):
        return(a)
    else:
        return (GCD(b,a%b))

baseRoopNum = int(input())

for i in range(baseRoopNum):
    inputList = [int(x) for x in input().split(" ")]
    fixedInputList = inputList[1:]
    
    combList = list(itertools.combinations(fixedInputList,r = 2))
    sum = 0
    for x in combList:
        sum += GCD(x[0],x[1])
    print(sum)
    
