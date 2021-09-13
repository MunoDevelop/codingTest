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
        tree[n + i] = arr[i]

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tmp = tree[i << 1] * tree[i << 1 | 1]
        if tmp > 0:
            tree[i] = 1
        elif tmp < 0:
            tree[i] = -1
        else:
            tree[i] = 0
        # print(f'tree[{i}] {tree[i]}')

# function to update a tree node
def updateTreeNode(p, value):
    # set value at position p
    tree[p + n] = value
    p = p + n
    # move upward and update parents
    i = p
    while i > 1:
        tmp = tree[i >> 1] = tree[i] * tree[i ^ 1]
        if tmp > 0:
            tree[i >> 1] = 1
        elif tmp < 0:
            tree[i >> 1] = -1
        else:
            tree[i >> 1] = 0
        i >>= 1

# function to get sum on interval [l, r)
def query(l, r):
    res = 1
    # loop to find the sum in the range
    l += n
    r += n
    while l < r:
        if (l & 1):
            res *= tree[l]
            l += 1
        if (r & 1):
            r -= 1
            res *= tree[r]
        l >>= 1
        r >>= 1
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0
    # return res

while True:
    try:
        N, Q = [int(x) for x in sys.stdin.readline().rstrip().split()]
        lt = [int(x) for x in sys.stdin.readline().rstrip().split()]
        n = len(lt)
        build(lt)
        tempLt = []
        for i in range(Q):
            c, a, b = [x for x in sys.stdin.readline().rstrip().split()]
            a = int(a)
            b = int(b)
            if c == "C":
                updateTreeNode(a - 1, b)
            elif c == "P":
                if query(a-1, b)>0:
                    tempLt.append("+")
                elif query(a-1, b) == 0:
                    tempLt.append("0")
                elif query(a-1, b) < 0:
                    tempLt.append("-")
        for i in tempLt:
            print(i,end="")
        print()
    except:
        break



