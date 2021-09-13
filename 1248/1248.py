import sys

N = int(input())
perm = list(range(-10,11))

g = [[0]*N for _ in range(N)]

tempI = [x for x in input()]
tempI.reverse()

for i in range(N):
    for j in range(N):
        if i>j:
            continue
        tmp = tempI.pop()
        if tmp=='+':
            g[i][j] = 1
        elif tmp == '-':
            g[i][j] = -1
        else:
            g[i][j] = 0
def sameSign(a,b):
    if a>0 and b>0:
        return True
    elif a<0 and b<0:
        return True
    elif a == 0 and b == 0:
        return True
    return False

class Found(Exception):pass

backList = [0]*N

def checkValid(depth):
    for i in range(depth+1):
        if not sameSign(sum(backList[i:depth+1]),g[i][depth]):
            return False
    return True
def backtrack(depth):
    if depth == N:
        for i in range(N):
            if i != N - 1:
                print(backList[i], end=" ")
            else:
                print(backList[i], end="")
        raise Found
    else:
        for j in perm:
            backList[depth] = j
            if checkValid(depth):
                backtrack(depth+1)
            backList[depth] = 0

try:
    backtrack(0)
    #checkValid()
except Found:
    None

# if not sameSign(sum(lt[i:j+1]),g[i][j]):
#     raise Found


