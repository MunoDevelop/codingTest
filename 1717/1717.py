import sys

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]


class DisjointSet:
    def __init__(self, n):
        self.data = [-1] * n
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


disjoint = DisjointSet(N + 1)

for i in range(M):
    lt = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if lt[0] == 0:
        disjoint.union(lt[1], lt[2])
    else:
        if disjoint.find(lt[1]) == disjoint.find(lt[2]):
            print("YES")
        else:
            print("NO")
