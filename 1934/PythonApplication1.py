def GCD(a,b):
    if(b==0):
        return(a)
    else:
        return (GCD(b,a%b))

baseRoopNum = int(input())

for i in range(baseRoopNum):
    inputList = [int(x) for x in input().split(" ")]
    a = inputList[0]
    b = inputList[1]


    gcd = GCD(a,b)
    lcm = int(a*b / gcd)
    print(lcm)
