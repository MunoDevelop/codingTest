def IsPrimeNumber(n):
	
	last = int(n / 2)
	if (n <= 1):
		return False
	for i in  range(2,last+1):
		if ((n%i) == 0):
			return False;
	return True


dummyNum = int(input())

inputList = [int(x) for x in input().split(" ")]

sum = 0
for x in inputList:
    if IsPrimeNumber(x):
        sum+=1
print(sum)
    
