import sys
import heapq

testCases = int(sys.stdin.readline().rstrip())

for case in range(testCases):
    N = int(sys.stdin.readline().rstrip())
    lt = []
    while N >10:
        lt.extend([int(x) for x in sys.stdin.readline().rstrip().split()])
        N-=10
    lt.extend([int(x) for x in sys.stdin.readline().rstrip().split()])
    minHeap = []
    maxHeap = []
    mid = 0
    ptLt = []
    for idx in range(len(lt)):
        i = lt[idx]
        # 높이 같을때
        if len(minHeap)==len(maxHeap):
            if i<mid:
                heapq.heappush(maxHeap,(-i,i))
                mid = maxHeap[0][1]
            else:
                heapq.heappush(minHeap,i)
                mid = minHeap[0]
        # 왼쪽이 더 많은 경우
        elif len(maxHeap) > len(minHeap):
            # 왼쪽이 더 많은데 왼쪽에 넣어야 하는 경우
            if i < mid:
                heapq.heappush(minHeap,heapq.heappop(maxHeap)[1])
                heapq.heappush(maxHeap,(-i,i))
            # 왼쪽이 더 많은데 오른쪽에 넣어야 하는 경우
            else:
                heapq.heappush(minHeap,i)

            mid = (minHeap[0] + maxHeap[0][1])//2
            # print(f'mid:{mid} minTop: {minHeap[0]} maxTop:{maxHeap[0][1]}')
        elif len(maxHeap) < len(minHeap):
            # 오른쪽이 더 많은데 왼쪽에 넣어야 하는 경우
            if i < mid:
                heapq.heappush(maxHeap,(-i,i))
            # 오른쪽이 더 많은데 오른쪽에 넣어야 하는 경우
            else:
                val = heapq.heappop(minHeap)
                heapq.heappush(maxHeap,(-val,val))
                heapq.heappush(minHeap,i)
            mid = (minHeap[0] + maxHeap[0][1])//2
            # print(f'mid:{mid} minTop: {minHeap[0]} maxTop:{maxHeap[0][1]}')
        if (idx+1)%2 == 1:
            ptLt.append(mid)
    print(len(ptLt))
    for i in range(len(ptLt)):
        if i == len(ptLt)-1:
            print(ptLt[i],end="")
        else:
            print(ptLt[i],end=" ")
    print()