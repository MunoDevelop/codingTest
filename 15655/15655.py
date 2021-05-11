def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next




N,M = map(int, input().split())

lst = sorted(list(map(int,input().split())))

for perm in sorted(combinations(lst,M)):
    #for i in range(1,len(perm)):
    #    if perm[i] < perm[i-1]:
    #        break
    #else:
    for token in perm:
        print(token,end = ' ')
    print(end = '\n')