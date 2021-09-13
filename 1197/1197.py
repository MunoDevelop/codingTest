import sys
import heapq

class DisjointSet:
    def __init__(self, n):
        self.data = [-1]*n
        self.size = n

    def find(self, index):
        value = self.data[index]
        if value < 0:
            return index

        return self.find(value)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] > self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x

        self.size -= 1


N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]

disjoint = DisjointSet(N)
que = []

for i in range(M):
    a, b ,c = [int(x) for x in sys.stdin.readline().rstrip().split()]
    heapq.heappush(que,(c, (a, b)))
    heapq.heappush(que,(c, (b, a)))
s = 0
while que:
    c,(a, b) = heapq.heappop(que)
    if disjoint.find(a-1) != disjoint.find(b-1):
        disjoint.union(a-1, b-1)
        s+=c
print(s)