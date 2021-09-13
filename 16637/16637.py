
def findSubState(subState, now, end):
    global oRange
    if now == end:
        for i in range(oRange-1):
            if subState[i] == subState[i+1] == 1:
                break
        else:
            process_solution(subState, end)
    else:
        subState[now] = 0
        findSubState(subState, now + 1, end)
        subState[now] = 1
        findSubState(subState, now + 1, end)
def process_solution(subState, end):
    global lt
    global S
    tempLt = lt[:]
    for ix in range(len(subState)):
        if subState[ix] == 1:
            opIdx = findIOperIdx(tempLt,ix)
            tempLt.insert(opIdx+2,')')
            tempLt.insert(opIdx-1,'(')
    stack = []
    for st in tempLt:
        if st in ['(','+','-','*']:
            stack.append(st)
        elif st != ')':
            if stack and stack[-1] in ['+','-','*']:
                oper = stack.pop()
                num1 = stack.pop()
                res = eval(''.join([num1,oper,st]))
                stack.append(str(res))
            else:
                stack.append(st)
        else:
            num = stack.pop()
            stack.pop()
            stack.append(num)
            while len(stack)>=3:
                num1 = stack.pop()
                oper = stack.pop()
                num2 = stack.pop()
                res = eval(''.join([num2, oper, num1]))
                stack.append(str(res))
    r = ''.join(tempLt)
    # print(tempLt)
    S = max(S,int(stack[0]))





def findIOperIdx(lt,n):
    k = 0
    for idx in range(len(lt)):
        if lt[idx] in ['+','-','*']:
            if n == k:
                return idx
            else:
                k+=1


N = int(input())
lt = list(input())


if N == 1:
    print(int(lt[0]))
else:
    oRange = N//2
    state = [0] * oRange
    S = int(-1e9)
    findSubState(state,0,len(state))
    print(S)

