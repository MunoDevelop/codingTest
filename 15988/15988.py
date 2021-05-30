M = int(input())
arr = [0] * 1000000
numList = list()
for i in range(M):
    numList.append(int(input()))

arr[0] = 1
arr[1] = 2
arr[2] = 4
for i in range(3, 1000000):
    arr[i] = (arr[i-1] + arr[i-2] + arr[i-3])%1000000009
for N in numList:
    print(arr[N-1])

