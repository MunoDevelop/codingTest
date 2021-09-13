import sys



# limit for array size
N = 1000000;

# Max size of tree
tree = [0] * (2 * N);

# from geek for geeks , little change

# function to build the tree
def build(arr):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = arr[i];

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[i << 1] , tree[i << 1 | 1])
        # print(f'tree[{i}] {tree[i]} =  i << 1-> {i << 1} * i << 1 | 1 ->{i << 1 | 1}')

# function to update a tree node
# def updateTreeNode(p, value):
#     # set value at position p
#     tree[p + n] = value;
#     p = p + n;
#     # move upward and update parents
#     i = p;
#     while i > 1:
#         tree[i >> 1] = tree[i] * tree[i ^ 1]%modVal;
#         i >>= 1;

# function to get sum on interval [l, r)
def query(l, r):
    res = int(1e10);
    # loop to find the sum in the range
    l += n;
    r += n;
    while l < r:
        if (l & 1):
            res = min(res,tree[l]);
            l += 1
        if (r & 1):
            r -= 1;
            res = min(res,tree[r]);
        l >>= 1;
        r >>= 1
    return res;


N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
lt = []
for i in range(N):
    lt.append(int(sys.stdin.readline().rstrip()))
n = len(lt)
build(lt)
for i in range(M):
    b, c = [int(x) for x in sys.stdin.readline().rstrip().split()]
    print(query(b-1, c))
