import sys

midfix = sys.stdin.readline().rstrip()
stack = []
for i in midfix[:]:
    if i == "(":
        stack.append(i)

    elif i == "*" or i == "/":
        while stack:
            if stack[-1] == "*" or stack[-1] == "/":
                print(stack.pop(),end="")
            else:
                break
        stack.append(i)
    elif i == "+" or i == "-":
        while stack:
            if stack[-1] == "(":
                break
            else:
                print(stack.pop(),end="")
        stack.append(i)
    elif i == ")":
        while stack:
            if stack[-1] == "(":
                stack.pop()
                break
            else:
                print(stack.pop(),end="")
    else:
        print(i,end="")
while stack:
    if stack[-1]!="(":
        print(stack.pop(),end="")