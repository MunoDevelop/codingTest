import sys
from bisect import bisect_left
inf = int(1e10)

N = int(sys.stdin.readline().rstrip())

A = [int(x) for x in sys.stdin.readline().rstrip().split()]

vec = [-inf]
lis = 0
for i in range(N):
    if A[i] > vec[-1]:
        vec.append(A[i])
        lis+=1
    else:
        vec[bisect_left(vec,A[i])] = A[i]


print(lis)