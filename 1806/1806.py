import sys

N,M = [int(x) for x in sys.stdin.readline().rstrip().split()]
lt = [int(x) for x in sys.stdin.readline().rstrip().split()]

s,e = 0,0
S = 0
Ans = 99999999

while True:
    if S>=M:
        if s<N:
            S-=lt[s]
            s+=1
        else:
            break
    else:
        if e<N:
            S += lt[e]
            e += 1
        else:
            break
    if S >= M:
        Ans = min(Ans,e-s)
if Ans == 99999999:
    print(0)
else:
    print(Ans)