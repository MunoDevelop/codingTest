import sys

n = int(sys.stdin.readline().rstrip())
s = 0
state = [0] * n

def findSubStateEx(now):
    global state
    global s
    global n
    if now == n:
        s+=1
    else:
        for i in range(n):
            ori = state[now]
            if promising(now,i):
                state[now] = i
                findSubStateEx(now+1)
            state[now] = ori


def promising(idx,current):
    global state
    for i in range(idx):
        if state[i] == current or abs(i - idx) == abs(state[i] - current):
            return False
    return True

findSubStateEx(0)
print(s)