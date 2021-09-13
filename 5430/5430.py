import sys
from collections import deque
cases = int(sys.stdin.readline())
for case in range(cases):
    operations = sys.stdin.readline().rstrip()
    ltLength = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().rstrip()
    start = 0
    if ltLength == 0:
        for i in operations:
            if i != "R":
                print("error")
                break
        else:
            print("[]")
    else:
        dq = deque([int(x) for x in line[1:len(line)-1].split(",")])
        for operate in operations:
            if operate == "R":
                if start == 0:
                    start = 1
                elif start == 1:
                    start = 0
            elif operate == "D":
                if start == 0:
                    if len(dq) > 0:
                        dq.popleft()
                    else:
                        print("error")
                        break
                elif start == 1:
                    if len(dq) > 0:
                        dq.pop()
                    else:
                        print("error")
                        break
        else:
            lt = []
            if start == 0:
                lt = list(dq)
            else:
                lt = list(reversed(dq))
            end = len(lt)-1
            print("[",end = "")
            for i in range(len(lt)):
                if i == end:
                    print(lt[i],end = "")
                else:
                    print(f'{lt[i]}',end = ",")
            print("]")