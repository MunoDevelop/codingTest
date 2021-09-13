import sys

N = int(input())
lt = [int(x) for x in input().split()]
K = int(input())

class Found(Exception):pass

def sol():
    global K
    start = 0
    for i in range(N-1):
        if K == 0:
            return
        idx = lt.index(max(lt[start:start+K+1]))
        # print(f'max :{lt}')
        if idx > 0:
            for j in range(idx-1,start-1,-1):
                # print(f'idx:{idx} k: {K}')
                lt[j],lt[j+1] = lt[j+1],lt[j]
                K-=1
        start+=1

sol()

for i in range(len(lt)):
    if i == N-1:
        print(f'{lt[i]}',end="")
    else:
        print(f'{lt[i]}', end=" ")