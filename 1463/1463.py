N = int(input())

arr = [-1] * (N+3)
arr[1] = 0
arr[2] = 1
arr[3] = 1

for i in range(2,N+1):
    if i%2 == 0 and i%3 == 0:
        arr[i] = min(arr[i - 1] + 1, arr[i // 2] + 1,arr[i//3]+1)
    elif i%3 == 0:
        arr[i] = min(arr[i - 1]+1, arr[i // 3]+1)
    elif i%2 == 0:
        arr[i]=min(arr[i-1]+1,arr[i//2]+1)
    else:
        arr[i] = arr[i-1]+1

print(arr[N])

