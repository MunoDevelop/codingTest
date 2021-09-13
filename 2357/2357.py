import sys



# limit for array size
N = 200000;

# Max size of tree

tree = [[0]*2 for _ in range(2 * N)]

# from geek for geeks , little change

# function to build the tree
def build(arr):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i][0] = arr[i]
        tree[n + i][1] = arr[i]

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i][0] = min(tree[i << 1][0] , tree[i << 1 | 1][0])
        tree[i][1] = max(tree[i << 1][1], tree[i << 1 | 1][1])

def query(l, r):
    res = int(1e10)
    res2 = 0
    # loop to find the sum in the range
    l += n
    r += n
    while l < r:
        if (l & 1):
            res = min(res,tree[l][0])
            res2 = max(res2,tree[l][1])
            l += 1
        if (r & 1):
            r -= 1
            res = min(res,tree[r][0])
            res2 = max(res2, tree[r][1])
        l >>= 1
        r >>= 1

    return res,res2;

N, M = [int(x) for x in sys.stdin.readline().rstrip().split()]
lt = []
for i in range(N):
    lt.append(int(sys.stdin.readline().rstrip()))
n = len(lt)
build(lt)

for i in range(M):
    b, c = [int(x) for x in sys.stdin.readline().rstrip().split()]
    a,b = query(b-1, c)
    print(f'{a} {b}')