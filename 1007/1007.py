cases = int(input())


def dist(a,b):
    return (a**2+b**2)**0.5


def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next


for case in range(cases):
    N = int(input())
    verts = []
    for i in range(N):
        verts.append(tuple([int(x) for x in input().split()]))
    pool = list(range(N))
    lt = []
    for selected in combinations(pool,N//2):
        x,y = 0,0
        for i in range(len(verts)):
            if i in selected:
                x += verts[i][0]
                y += verts[i][1]
            else:
                x -= verts[i][0]
                y -= verts[i][1]
        lt.append(dist(x,y))
    print(min(lt))
