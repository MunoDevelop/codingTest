import sys

sys.setrecursionlimit(10**6)
N = int(input())

g = [[] for _ in range(N)]
for i in range(N):
    temp = [int(x) for x in sys.stdin.readline().rstrip().split()[:-1]]
    ix = temp[0]-1
    for j in range(1,len(temp)-1,2):
        # print(f'loop {i} {i} to {temp[j]-1} cost {temp[j+1]}')
        g[ix].append((temp[j]-1,temp[j+1]))
        # g[temp[i]-1].append((i,temp[i+1]))
    # g[i] = [int(x) for x in sys.stdin.readline().rstrip().split()]
    # g[i].pop()
# print(g)

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
