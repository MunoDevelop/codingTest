import itertools
#sys.stdin = open("input.txt", "r")
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    if test_case >1:
        break
    nList = list()
    for i in range(9):
        nList.append(int(input()))
    combList = list(itertools.combinations(nList,2))
    for i in combList :
        vList = nList[:]
        del vList[vList.index(i[0])]
        del vList[vList.index(i[1])]
        if sum(vList)==100:
            vList.sort()
            for i in vList:
                print(i)
            break
    # ///////////////////////////////////////////////////////////////////////////////////
