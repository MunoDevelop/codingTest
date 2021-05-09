def combinations_with_replacement(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:],r-1):
                if arr[i]<=next[0]:
                    yield [arr[i]] + next



N,M = map(int, input().split())

lst = [x for x in range(1,N+1)]

for perm in combinations_with_replacement(lst,M):
    for token in perm:
        print(token,end = ' ')
    print(end = '\n')