cases = int(input())
for case in range(cases):
    lt = [x for x in input().split("X")]
    s = 0
    for i in lt:
        n =len(i)
        s+=(n*(n+1)//2)
    print(s)
