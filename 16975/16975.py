import sys

# si -> current index
def updateRangeUtil(si, ss, se, us, ue, diff):

    # 업뎃 해야될게 남아있으면 우선 업뎃
    if (lazy[si] != 0):
        tree[si] += (se - ss + 1) * lazy[si]
        # 잎 노드 아닐때만 아랫층에 lazy를 물려준다
        if (ss != se):
            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2 + 2] += lazy[si]

        lazy[si] = 0

    if (ss > se or ss > ue or se < us):
        return

    # 오버랩이 아니라 범위에 포함
    if (ss >= us and se <= ue):
        tree[si] += (se - ss + 1) * diff

        if (ss != se):
            lazy[si * 2 + 1] += diff
            lazy[si * 2 + 2] += diff
        return

    # 오버랩
    mid = (ss + se) // 2
    updateRangeUtil(si * 2 + 1, ss,
                    mid, us, ue, diff)
    updateRangeUtil(si * 2 + 2, mid + 1,
                    se, us, ue, diff)

    tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2]

def updateRange(n, us, ue, diff):
    updateRangeUtil(0, 0, n - 1, us, ue, diff)

def getSumUtil(ss, se, qs, qe, si):
    if (lazy[si] != 0):
        # si 는 ss to se 표시함
        tree[si] += (se - ss + 1) * lazy[si]
        # 잎 노드 아닐때만 아랫층에 lazy를 물려준다
        if (ss != se):
            lazy[si * 2 + 1] += lazy[si]
            lazy[si * 2 + 2] += lazy[si]

        lazy[si] = 0

    if (ss > se or ss > qe or se < qs):
        return 0

    # 범위안에 있으면 윗층의 오버랩에서 온거니까 바로 출력
    if (ss >= qs and se <= qe):
        return tree[si]

        # 오버랩
    mid = (ss + se) // 2
    return (getSumUtil(ss, mid, qs, qe, 2 * si + 1) +
            getSumUtil(mid + 1, se, qs, qe, 2 * si + 2))

# 쓰기 편하게 포장
def getSum(n, qs, qe):
    if (qs < 0 or qe > n - 1 or qs > qe):
        print("Invalid Input")
        return -1

    return getSumUtil(0, n - 1, qs, qe, 0)

def constructSTUtil(arr, ss, se, si):
    if (ss > se):
        return
    # 한개만 있는 경우는 저장하면 됨
    if (ss == se):
        tree[si] = arr[ss]
        return

    mid = (ss + se) // 2
    constructSTUtil(arr, ss, mid, si * 2 + 1)
    constructSTUtil(arr, mid + 1, se, si * 2 + 2)

    tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2]
# 쓰기 쉽게 포장
def constructST(arr, n):
    # Fill the allocated memory st
    constructSTUtil(arr, 0, n - 1, 0)


MAX = 100000*4
# from geeks for geeks , changed little, learned
tree = [0] * MAX
lazy = [0] * MAX

N = int(input())

lt = [int(x) for x in sys.stdin.readline().rstrip().split()]

M = int(input())
constructST(lt,N)

for i in range(M):
    tempLt = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if tempLt[0] == 1:
        updateRange(N,tempLt[1]-1,tempLt[2]-1,tempLt[3])
    else:
        print(getSum(N,tempLt[1]-1,tempLt[1]-1))

