import itertools

N = int(input())

lt = list()
for i in range(1,N+1):
    lt.append(i)
permuList = list(itertools.permutations(lt,N))
for i in range(len(permuList)):
    for j in range(len(permuList[i])):
        print('{0}'.format(permuList[i][j]),end = " ")
    print("")
