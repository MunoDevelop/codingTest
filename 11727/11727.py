N = int(input())

arr = [0] * N
arr[0] = 1
if N > 1:
    arr[1] = 3
for i in range(2, N):
    arr[i] = arr[i-1] + arr[i-2]*2

print(arr[-1]%10007)

