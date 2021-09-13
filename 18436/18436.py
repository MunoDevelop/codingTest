import sys

# limit for array size
N = 1000000

# Max size of tree
tree = [0] * (2 * N)

# from geek for geeks , little change

# function to build the tree
def build(arr):
    # insert leaf nodes in tree
    for i in range(n):
        if arr[i]%2 == 1:
            tree[n + i] = 1
        else:
            tree[n + i] = 0

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
        # print(f'tree[{i}] {tree[i]} =  i << 1-> {i << 1} * i << 1 | 1 ->{i << 1 | 1}')


def updateTreeNode(p, value):
    if value%2 == 1:
        value = 1
    else:
        value = 0
    # set value at position p
    tree[p + n] = value
    p = p + n
    # move upward and update parents
    i = p
    while i > 1:
        tree[i >> 1] = tree[i]+tree[i ^ 1]
        i >>= 1

# function to get sum on interval [l, r)
def query(l, r):
    res = 0
    # loop to find the sum in the range
    l += n
    r += n
    while l < r:
        if (l & 1):
            res += tree[l]
            l += 1
        if (r & 1):
            r -= 1
            res += tree[r]
        l >>= 1
        r >>= 1
    return res


N = int(sys.stdin.readline().rstrip())
lt = [int(x) for x in sys.stdin.readline().rstrip().split()]
Q = int(sys.stdin.readline().rstrip())
n = len(lt)
build(lt)
for i in range(Q):
    c, a, b = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if c == 1:
        updateTreeNode(a - 1, b)
    elif c == 2:
        print((b+1-a)-query(a-1, b))
    elif c == 3:
        print(query(a - 1, b))
