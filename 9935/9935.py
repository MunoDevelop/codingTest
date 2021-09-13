import sys

sList = [x for x in sys.stdin.readline().rstrip()]
bombList = [x for x in sys.stdin.readline().rstrip()]

stack = []
for i in sList:
    stack.append(i)
    signal = False
    while len(stack)>=len(bombList):
        if signal:
            break
        for i in range(1,len(bombList)+1):
            if bombList[-i]!=stack[-i]:
                signal = True
                break
        else:
            for i in range(len(bombList)):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))