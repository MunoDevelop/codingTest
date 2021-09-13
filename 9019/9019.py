import sys
from collections import deque


def cal(a, operate):
    if operate == 'D':
        return (a * 2) % 10000
    elif operate == 'S':
        if a == 0:
            return 9999
        else:
            return a - 1
    elif operate == 'L':
        return (a % 1000) * 10 + a // 1000
    elif operate == 'R':
        return a // 10 + (a % 10) * 1000


visited = [False] * 10000
cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    start, dest = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if start == dest:
        print()
        continue
    pathList = []
    pathList.append(0)
    queue = deque()
    for i in range(10000):
        visited[i] = False
    queue.append((0, 'D', cal(start, 'D')))
    queue.append((0, 'S', cal(start, 'S')))
    queue.append((0, 'L', cal(start, 'L')))
    queue.append((0, 'R', cal(start, 'R')))
    while queue:
        temp = queue.popleft()
        pathList.append((temp[0], temp[1]))
        idx = len(pathList) - 1
        if temp[2] == dest:
            lst = []
            while idx != 0:
                lst.append(pathList[idx][1])
                idx = pathList[idx][0]
            print(''.join(reversed(lst)))
            break
        else:
            res = cal(temp[2],'D')
            if not visited[res-1]:
                visited[res - 1] = True
                queue.append((idx,'D',res))
            res = cal(temp[2], 'S')
            if not visited[res - 1]:
                visited[res - 1] = True
                queue.append((idx, 'S', res))
            res = cal(temp[2], 'L')
            if not visited[res - 1]:
                visited[res - 1] = True
                queue.append((idx, 'L', res))
            res = cal(temp[2], 'R')
            if not visited[res - 1]:
                visited[res - 1] = True
                queue.append((idx, 'R', res))

