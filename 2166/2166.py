import sys

N = int(sys.stdin.readline().rstrip())
verts = []
for i in range(N):
    verts.append([int(x) for x in sys.stdin.readline().rstrip().split()])
#verts.sort(key= lambda ele:(ele[0],ele[1]))
origin = verts[0]
S = 0
j = N-1 # last vertex
for i in range(N):
    S += (verts[j][0]+verts[i][0])*(verts[j][1]-verts[i][1])
    j = i # save i
print(abs(S/2))