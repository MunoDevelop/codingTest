def product(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr,r-1):
                yield [arr[i]] + next


N,M = map(int, input().split())

lst = [x for x in range(1,N+1)]

for perm in sorted(product(lst,M)):
    #for i in range(1,len(perm)):
    #    if perm[i] <= perm[i-1]:
    #        break
    #else:
    for token in perm:
        print(token,end = ' ')
    print(end = '\n')