import sys
from bisect import bisect_left
inf = int(1e10)

N = int(sys.stdin.readline().rstrip())

A = [int(x) for x in sys.stdin.readline().rstrip().split()]

vec = [-inf]
lis = 0
idxList = []
for i in range(N):
    if A[i] > vec[-1]:
        idxList.append(len(vec))
        vec.append(A[i])
        lis += 1
    else:
        idx = bisect_left(vec,A[i])
        idxList.append(idx)
        vec[idx] = A[i]
lt = []

temp = lis
for i in range(N-1,-1,-1):
    if temp == 0:
        break
    if idxList[i] == temp:
        lt.append(i)
        temp -= 1
lt.reverse()

lt = [A[i] for i in lt]

print(lis)
for i in range(len(lt)):
    if i == len(lt)-1:
        print(f'{lt[i]}',end="")
    else:
        print(f'{lt[i]}', end=" ")