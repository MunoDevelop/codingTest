import sys

N = int(input())
S = 0

lt = []
for i in range(N):
    a, b = [int(x) for x in sys.stdin.readline().rstrip().split()]
    lt.append((a, b))
lt.sort()
pa, pb = 0, 0
for a, b in lt:
    if (pa, pb) == (0, 0):
        pa, pb = a, b
    else:
        if a < pb:
            pb = max(b, pb)
        elif pa <= a < b <= pb:
            continue
        else:
            S += (pb - pa)
            pa, pb = a, b

print(S + (pb - pa))
