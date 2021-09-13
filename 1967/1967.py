import sys

sys.setrecursionlimit(10**6)
N = int(input())

g = [[] for _ in range(N)]
for i in range(N-1):
    a,b,dis = [int(x) for x in sys.stdin.readline().rstrip().split()]
    a -= 1
    b-=1
    g[a].append((b,dis))
    g[b].append((a,dis))



visited = [False]*N
depthRecords = [0]*N
def dfs(idx,distSum):
    for node,dist in g[idx]:
        if not visited[node]:
            visited[node] = True
            depthRecords[node] = distSum+dist
            dfs(node,distSum+dist)

visited[0] = True
dfs(0,0)

idx1 = depthRecords.index(max(depthRecords))
visited = [False]*N
visited[idx1] = True
depthRecords = [0]*N
dfs(idx1,0)


idx2 = depthRecords.index(max(depthRecords))
visited = [False]*N
visited[idx2] = True
depthRecords = [0]*N
dfs(idx2,0)
# print(depthRecords)
print(depthRecords[idx1])
