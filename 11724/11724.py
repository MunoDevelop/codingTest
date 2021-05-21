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


N, M = map(int, input().split())

disjoint = DisjointSet(N)
for i in range(M):
    a, b = map(int, input().split())
    disjoint.union(a-1, b-1)

print(disjoint.size)
