import math
import sys
def IsPrimeNumber(n):
	
	last = int(math.sqrt(n))
	if (n <= 1):
		return False
	for i in  range(2,last+1):
		if ((n%i) == 0):
			return False;
	return True

primeList = list()
for i in range(2,10000):
    if IsPrimeNumber(i):
        primeList.append(i)

for x in range(1,100001):
    inputNum = int(sys.stdin.readline())
    if(inputNum!=0):
        for i in primeList:
            if IsPrimeNumber(inputNum-i):
                print('{0} = {1} + {2}'.format(inputNum,i,inputNum-i))
                break
    else:break
