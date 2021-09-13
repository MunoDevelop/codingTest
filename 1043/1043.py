import sys

n,p = [int(x) for x in sys.stdin.readline().rstrip().split()]

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

tList = [int(x) for x in sys.stdin.readline().rstrip().split()]
Ans = 0
if tList[0] == 0:
    print(p)
else:
    partyList = []
    disjoint = DisjointSet(n)
    linkerIdx = tList[1]-1
    for val in tList[1:]:
        disjoint.union(linkerIdx,val-1)

    for pIdx in range(p):
        nLt = [int(x) for x in sys.stdin.readline().rstrip().split()]
        if nLt[0] == 0:
            continue
        else:
            partyLinker = nLt[1]-1
            # binding
            for i in nLt[1:]:
                if disjoint.find(linkerIdx) == disjoint.find(i-1):
                    disjoint.union(linkerIdx, partyLinker)
                else:
                    disjoint.union(partyLinker,i-1)
            partyList.append(nLt[1:])
    for party in partyList:
        flag = True
        for p in party:
            if disjoint.find(linkerIdx) == disjoint.find(p-1):
                flag = False
        if flag:
            Ans+=1
    print(Ans)
    #print(f'{disjoint.size} {Ans}')