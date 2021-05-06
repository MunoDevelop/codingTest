def permutations(arr,r,prefix = [],k = 0):
    if len(prefix) == r:
        yield prefix
    else:
        for i in range(k,len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permutations(arr,r,prefix + [arr[k]], k+1):
                yield next
            arr[i], arr[k] = arr[k], arr[i]


N,M = map(int, input().split())

lst = [x for x in range(1,N+1)]

for perm in sorted(permutations(lst,M)):
    for token in perm:
        print(token,end = ' ')
    print(end = '\n')