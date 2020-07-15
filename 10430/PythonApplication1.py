import itertools

def GCD(a,b):
    if(b==0):
        return(a)
    else:
        return (GCD(b,a%b))

baseRoopNum = int(input())

for i in range(baseRoopNum):
    inputList = [int(x) for x in input().split(" ")]
    #fixedInputList = inputList[1:3]
    #print(inputList)
    #print(list(itertools.combinations(fixedInputList,r = 2)))
    

    #gcd = GCD(a,b)
    #lcm = int(a*b / gcd)
    #print(lcm)
