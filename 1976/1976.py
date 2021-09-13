import sys


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



N = int(input())
M = int(input())

disjoint = DisjointSet(N)

g = [[0]*N for _ in range(N)]

for i in range(N):
    g[i] = [int(x) for x in sys.stdin.readline().rstrip().split()]


for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            disjoint.union(i, j)

lt = [int(x)-1 for x in sys.stdin.readline().rstrip().split()]
idx = disjoint.find(lt[0])
for i in lt[1:]:
    if disjoint.find(i) != idx:
        print("NO")
        break
else:
    print("YES")

