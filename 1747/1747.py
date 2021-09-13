import sys

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

N = int(input())
primeLt = {}
for i in solution(1,2000000):
    primeLt[i] = 0


def isPalin(num):
    lt = [int(x) for x in str(num)]
    for i in range(len(lt)//2):
        if lt[i]!=lt[-(i+1)]:
            return False
    return True

for i in range(N,N+1000000):
    if i in primeLt and isPalin(i):
        print(i)
        break
