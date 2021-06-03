N = int(input())

k = 0
for i in range(1,N+1):
    k += (N//i)*i

print(k)