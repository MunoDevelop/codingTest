def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr, r - 1):
                yield [arr[i]] + next


N, M = map(int, input().split())

lst = sorted(list(map(int, input().split())))

iSet = set()
for perm in sorted(product(lst, M)):
    # for i in range(1,len(perm)):
    #    if perm[i] < perm[i-1]:
    #        break
    # else:
    if ' '.join(map(str, perm)) not in iSet:
        for token in perm:
            print(token, end=' ')
        print(end='\n')
        iSet.add(' '.join(map(str, perm)))

