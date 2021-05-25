import sys


def valid_index(i):
    if i in range(100001):
        return True
    else:
        return False


def valid_neighbors(i):
    lst = []

    if valid_index(i+1) and visited[i+1] == -1:
        lst.append(i+1)
    if valid_index(i-1) and visited[i-1] == -1:
        lst.append(i-1)
    if valid_index(i*2) and visited[i*2] == -1:
        lst.append(i*2)
    return lst


def bfs(i, j):
    if i == j:
        return 0
    queue.append(i)
    visited[i] = -2
    #print(v+1,end = ' ')
    depth = 0
    while len(queue) != 0:

        v = queue.pop(0)
        for k in valid_neighbors(v):
            if k == j:
                depth += 1
                while visited[v] != -2:
                    depth += 1
                    #print(v)
                    v = visited[v]
                return depth
            queue.append(k)
            visited[k] = v


N, M = map(int, input().split())

#g = [0 for _ in range(max(N, M)+1)]

visited = [-1 for _ in range(100001)]
queue = []

print(bfs(N, M))
#area.sort()

