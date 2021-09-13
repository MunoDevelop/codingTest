import sys
N = int(input())
lt = sorted([int(x) for x in sys.stdin.readline().rstrip().split()])

s,e = 0,N-1
S = lt[s]+lt[e]
minS = abs(S)
Ans = (0,N-1)
while s<e:
    if abs(lt[s]+lt[e])<minS:
        S = lt[s]+lt[e]
        Ans = (s, e)
        minS = abs(S)
    else:
        S = lt[s] + lt[e]
    if S > 0:
        e-=1
        # print("e-1")
    elif S<0:
        s+=1
        # print("s+1")
    else:
        break
print(f'{lt[Ans[0]]} {lt[Ans[1]]}')