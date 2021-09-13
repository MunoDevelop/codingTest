import sys


class SegTree:
    # from github , little change
    def __init__(self,Arr):
        self.A = Arr
        self.tree = [0] * 4 * len(Arr)
        self.init_recur(1, 0, len(Arr))
        self.N = len(Arr)

    def init_recur(self, node, left, right):
        if left + 1 == right:
            # print(f'left {left} set to {self.A[left]}')
            self.tree[node] = self.A[left]
        else:
            mid = (left + right) // 2
            # print(f'left {left} mid {mid} mid {mid} right {right}')
            self.tree[node] = self.init_recur(node * 2, left, mid) + self.init_recur(node * 2 + 1, mid, right)
        return self.tree[node]

    #
    def sum(self, idx_start, idx_end):
        def sum_recur(self, node, left, right, start, end):
            if start <= left and right <= end:
                return self.tree[node]
            if right<=start or end<=left:
                return 0
            mid = (left+right)//2
            return sum_recur(self,node * 2, left, mid, start, end) + sum_recur(self,node * 2 + 1, mid, right, start, end)
        return sum_recur(self, 1, 0, self.N, idx_start, idx_end + 1)

    def update(self,target_idx,value):
        gap = value-self.A[target_idx]
        def update_recur(self, node, left, right, target, val):
            if left<=target<right:
                self.tree[node] += val
                if left+1 == right: return
                mid = (left+right)//2
                update_recur(self,node * 2, left, mid, target, val)
                update_recur(self,node * 2 + 1, mid, right, target, val)
        update_recur(self,1,0,self.N,target_idx,gap)
        self.A[target_idx] = value

N,M = [int(x) for x in sys.stdin.readline().rstrip().split()]
lt = [0]*N



seg = SegTree(lt)

for i in range(M):
    a,b,c = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if a == 1:
        seg.update(b-1,c)
    else:
        # print(f'{seg.A}')
        # print(f'sum: {b - 1} {c - 1}')
        if b>c:
            b,c = c,b
        print(seg.sum(b-1,c-1))
#
# Seg1=SegTree([1,2,3,4,5,4,3,2,1])
# Seg1.update(7,2)
# Seg1.update(8,2)
# print(Seg1.sum(7,8))
