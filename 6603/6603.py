import itertools

while True:
    inPutLine = [int(x) for x in input().split()]
    if inPutLine[0] == 0:
        break
    k = inPutLine[0]
    s = inPutLine[1:]
    lt = list()
    lt = list(itertools.combinations(s,6))
    for k in lt:
        for i in k:
            print(i,end = " ")
        print()
    print()