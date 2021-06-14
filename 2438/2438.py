n = int(input())

for i in range(n+1):
    for j in range(i):
        if j == i-1:
            print("*",end="\n")
        else:
            print("*", end="")