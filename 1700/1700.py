import time

N,K = [int(x) for x in input().split()]

lt = [int(x) for x in input().split()]

multab = []
cnt = 0

for idx in range(len(lt)):
    if lt[idx] in multab:
        # print(f'{lt[idx]} exist in tab')
        continue
    # if have space
    if len(multab) < N:
        multab.append(lt[idx])
        # print(f'tab add {lt[idx]}')
    else:
        # if sth in multab not use any more
        restLt = lt[idx:]
        tempIx = 0
        for sth in multab:
            if sth not in restLt:
                tempIx = sth
                break
        # not use
        if tempIx != 0:
            multab.remove(tempIx)
            # print(f'tab remove {tempIx}')
            multab.append(lt[idx])
            cnt+=1
        # everything will use, so check order
        else:
            tempLt = []
            for sth in multab:
                ix = restLt.index(sth)
                tempLt.append((ix,sth))
            tempLt.sort(key=lambda ele:(-ele[0]))
            # print(tempLt)
            multab.remove(tempLt[0][1])
            multab.append(lt[idx])
            # print(f'tab remove {tempLt[0][1]} and add ')
            cnt+=1

print(cnt)