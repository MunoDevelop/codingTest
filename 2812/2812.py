import sys

N, K = [int(x) for x in sys.stdin.readline().rstrip().split()]
lt = [int(x) for x in sys.stdin.readline().rstrip()]
stack = []
for i in lt:

    if len(stack) == 0:
        # print(f'append {i}')
        stack.append(i)
    else:
        while stack and stack[-1] < i and K > 0:
            stack.pop()
            K -= 1
        # print(f'append {i}')
        stack.append(i)
if K > 0:
    while K > 0:
        stack.pop()
        K -= 1

stack = [str(x) for x in stack]
print(''.join(stack))
