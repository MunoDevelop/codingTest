import sys
iLt = [int(x) for x in input().split()]
M = iLt[0]
N = iLt[1]

def solution(k,n):
    #from wiki,fixed
    answer = 0
    sieve = [True]*(n+1)
    sieve[1] = [False]
    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(2*i,n+1,i):
                sieve[j] = False
    return [i for i in range(k,n+1) if sieve[i] == True]
for i in solution(M,N):
    print(i)