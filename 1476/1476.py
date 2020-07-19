import math
import sys

inputList = [int(x) for x in input().split(" ")]
eNum = inputList[0]
sNum = inputList[1]
mNum = inputList[2]

for i in range(1,100000):
    if (i-eNum)%15==0 and (i-sNum)%28==0 and (i-mNum)%19==0:
        print(i)
        break

