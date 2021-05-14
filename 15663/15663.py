def permutations(arr, r, prefix=[], k=0):
    if len(prefix) == r:
        yield prefix
    else:
        for i in range(k, len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permutations(arr, r, prefix + [arr[k]], k + 1):
                yield next
            arr[i], arr[k] = arr[k], arr[i]


N, M = map(int, input().split())

lst = sorted(list(map(int, input().split())))

iSet = set()
for perm in sorted(permutations(lst, M)):
    # for i in range(1,len(perm)):
    #    if perm[i] < perm[i-1]:
    #        break
    # else:
    if ' '.join(map(str, perm)) not in iSet:
        for token in perm:
            print(token, end=' ')
        print(end='\n')
        iSet.add(' '.join(map(str, perm)))

