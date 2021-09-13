import sys
import heapq

N = int(input())
hq = []

for i in range(N):
    k = int(sys.stdin.readline().rstrip())
    heapq.heappush(hq,k)
s = 0
while len(hq)>1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    s+=(a+b)
    heapq.heappush(hq,a+b)

print(s)