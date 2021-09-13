import sys
from bisect import bisect_left
import bisect

N = int(input())
lt = []

for i in range(N):
    temp = [int(x) for x in input().split()]
    for i in temp:
        bisect.insort(lt,i)
        if len(lt)>N:
            lt.remove(lt[0])


print(lt[-N])