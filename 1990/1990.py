import sys


def isPalin(num):
    lt = [int(x) for x in str(num)]
    for i in range(len(lt)//2):
        if lt[i]!=lt[-(i+1)]:
            return False
    return True

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
                
    for i in range(N,M+1):
        # trick , have no choice
        if i >= 10000000:
            break
        if sieve[i] == True and isPalin(i):
            print(i)
    print(-1)
    # return [i for i in range(k,n+1) ]

N,M = [int(x) for x in input().split()]


solution(1,10000000)



#
# for i in range(N,N+1000000):
#     if i in primeLt and isPalin(i):
#         print(i)
#         break
