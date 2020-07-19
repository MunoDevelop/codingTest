def isDesc(lt):
    for i in range(len(lt)-1):
        if(lt[i]<lt[i+1]):
            return False
    return True

def printList(lt):
    for i in range(len(lt)):
        print('{0}'.format(lt[i]),end = " ")

N  = int(input())
lt = [int(x) for x in input().split(" ")]
nextPermu = list()
if N==1:
    print(-1)
elif N==2:
    if isDesc(lt):
        print(-1)
    else:
        nextPermu.append(lt[-1])
        nextPermu.append(lt[-2])
        printList(nextPermu)
else:
    if isDesc(lt):
        print(-1)
    else:
        for i in range(N):
            if isDesc(lt[i+1:]):
                if i > 0:
                    for j in lt[:i]:
                        nextPermu.append(j)
                for k in lt[-1:i:-1]:
                    if lt[i] < k:
                        nextPermu.append(k)
                        break
                for l in range(len(nextPermu)):
                    lt.remove(nextPermu[l])
                lt.sort()
                for m in lt:
                    nextPermu.append(m)
                printList(nextPermu)
                break
       