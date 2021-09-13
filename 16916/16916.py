import sys

#from geeks for geeks ,changed little

def kmp(txt,pat):
    m,n = len(pat),len(txt)
    # 패턴길이 배열, 해당 위치 i 에서 가장 긴 prefix==suffix 길이를 저장
    lps = [0]*m
    # pat 인덱스
    j = 0
    ptIdxList = []
    computeLPSArray(pat,m,lps)
    # text 인덱스
    i = 0
    while i<n:
        if pat[j] == txt[i]:
            i+=1
            j+=1
        if j == m:
            ptIdxList.append(i-j)
            j = lps[j-1]
        elif i<n and pat[j] != txt[i]:
            # lps[j-1] make sense
            if j != 0:
                j = lps[j-1]
            else:
                i+=1
    return ptIdxList
pm = 0
def computeLPSArray(pat,m,lps):
    global pm
    preLen = 0
    i = 1
    # lps[0] = 0, lps[1] = 1 if pat[0] == pat[1],...
    while i<m:
        #
        if pat[i] == pat[preLen]:
            preLen+=1
            # print(preLen)
            pm = max(pm,preLen)
            lps[i] = preLen
            i+=1
        else:
            # 다른데 이전에 같은부분이 존재했던 경우
            if preLen != 0:
                preLen = lps[preLen-1]
            # 다르고 이전에도 같은 부분은 없는 경우
            else:
                lps[i] = 0
                i += 1

txt = sys.stdin.readline().rstrip()

pat = sys.stdin.readline().rstrip()
lt = kmp(txt, pat)
if len(lt)>0:
    print(1)
else:
    print(0)
# print(len(lt))
# for idx in lt:
#     print(idx+1)


