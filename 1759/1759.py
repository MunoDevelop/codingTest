import itertools
import copy
L = int(list(input().split())[0])
pool = input().split()
pool.sort()
C = len(pool)
stack = list()

def check(stack):
    sum = 0
    sum += stack.count('a')
    sum += stack.count('e')
    sum += stack.count('i')
    sum += stack.count('o')
    sum += stack.count('u')
    if sum > 0 and L-sum >1:
        return True
    else: 
        return False

# depth 1 start
def DFS():
    if len(stack) == L:
        if check(stack):
            for i in stack:
                print(i,end = "")
            print()
            return
        else:  
            return
    else:
        
        for i in [x for x in pool if x not in stack]:
            if len(stack)>0 and stack[-1] > i:
                continue
            stack.append(i)
            DFS()
            stack.pop()

DFS()