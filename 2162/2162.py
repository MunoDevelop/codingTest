import sys
from collections import Counter
def ccw(x1,y1,x2,y2,x3,y3):
    val = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    if val > 0:
        # 반시계
        return 1
    elif val == 0:
        # 일직선
        return 0
    elif val < 0:
        # 시계 방향
        return -1

def cross(x1,y1,x2,y2,x3,y3,x4,y4):
    if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<=0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)<=0:
        if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)==0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)==0:
            # make sure a<b and c<d
            if (x1,y1)>(x2,y2):
                x1,y1,x2,y2 = x2,y2,x1,y1
            if (x3,y3)>(x4,y4):
                x3,y3,x4,y4 = x4,y4,x3,y3
            # when a<d and b>c
            if (x1,y1)<=(x4,y4) and (x3,y3)<=(x2,y2):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

class DisjointSet:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n

    def upward(self, change_list, index):
        value = self.data[index]
        if value < 0:
            return index

        change_list.append(index)
        return self.upward(change_list, value)

    def find(self, index):
        change_list = []
        result = self.upward(change_list, index)

        for i in change_list:
            self.data[i] = result

        return result

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] < self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x

        self.size -= 1


N = int(input())

disj = DisjointSet(N)

lineList = []

for i in range(N):
    lineList.append([int(x) for x in sys.stdin.readline().rstrip().split()])

for i in range(N-1):
    a = lineList[i]
    for j in range(i+1,N):
        b = lineList[j]
        if cross(a[0],a[1],a[2],a[3],b[0],b[1],b[2],b[3]):
            disj.union(i,j)
print(disj.size)
lt = []

for i in range(N):
    lt.append(disj.find(i))
print(Counter(lt).most_common()[0][1])