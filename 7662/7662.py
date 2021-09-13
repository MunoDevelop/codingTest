import sys
def solution(operations):
    dic = {}

    for op in operations:
        lt = op.split()
        if lt[0] == 'I':
            i = int(lt[1])
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        elif lt[0] == 'D':
            if len(dic)>0:
                if lt[1] == '1':
                    k = max(dic)
                    dic[k] -= 1
                    if dic[k]==0:
                        del dic[k]
                else:
                    k = min(dic)
                    dic[k] -= 1
                    if dic[k]==0:
                        del dic[k]
    if len(dic) == 0:
        print("EMPTY")
    else:
        print(f'{max(dic)} {min(dic)}')
    return 0

cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
    operations = []
    N = int(sys.stdin.readline().rstrip())
    for i in range(N):
        operations.append(sys.stdin.readline().rstrip())
    solution(operations)

