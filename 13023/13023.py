import sys

def dfs(graph, v, visited, depth):
    visited[v] = True
    #print(v,end = ' ')
    #print('depth:'+str(depth))
    if depth == 4:
        print(1)
        sys.exit()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited,depth+1)
    visited[v] = False

N, M = map(int, input().split())

graph = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

visited = [False]*N
for i in range(N):
    dfs(graph,i,visited,0)
    visited = [False]*N
print(0)