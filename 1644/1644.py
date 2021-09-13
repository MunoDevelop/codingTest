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


M = int(sys.stdin.readline().rstrip())
lt = solution(1,M)
N = len(lt)


s,e = 0,0
S = 0
Ans = 0
while True:
    if S>=M:
        S-=lt[s]
        s+=1
    else:
        if e<N:
            S += lt[e]
            e += 1
        else:
            break
    if S == M:
        Ans+=1
print(Ans)