
n,m,start = map(int,input().split())
g = [[0 for x in range(n)] for y in range(n)]
# valid self
for i in range(n):
    g[i][i] = 1

stack = []
visited = [0]*n
#시작정점의 번호는 1번부터 있을때
v=start -1
for i in range(m):
    s,e = map(int,input().split())
    s-=1
    e-=1

    g[s][e] = 1
    g[e][s] = 1

def ValidNeighbors(v,re = False):
    lst = []
    for i in range(n):
        if g[v][i]==1 and visited[i] == 0:
            lst.append(i)
    if re:
        return sorted(lst,reverse = True)
    else:
        return sorted(lst)



def dfs_iterative(v):
    stack.append(v)
    while len(stack)>0:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            print(v+1,end = ' ')
            for i in ValidNeighbors(v,True):
                stack.append(i)

queue = []


def bfs(v):
    queue.append(v)
    visited[v] = 1
    print(v+1,end = ' ')
    while len(queue)!=0:
        v = queue.pop(0)
        for i in ValidNeighbors(v):
            queue.append(i)
            visited[i] = 1
            print(i+1,end = ' ')


dfs_iterative(v)
print('',end = '\n')
# visited reset
visited = [0]*n
v=start -1
bfs(v)
