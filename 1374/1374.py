import sys
import heapq

N = int(input())

sq = []
eq = []

for i in range(N):
    # 시작 기준 sq 넣고 종료기준 eq 넣는다
    no,s,e = [int(x) for x in sys.stdin.readline().rstrip().split()]
    # sq.put((s, e))
    heapq.heappush(sq, (s, e))
    # eq.put((e, s))
    heapq.heappush(eq, (e, s))
t = 0
room = 0
roomMax = 0
while sq:
    # t = sq.get()[0]
    t = heapq.heappop(sq)[0]
    # 새로운 강의실이 필요할때 t를 조정하고 t보다 작은 원소 pop
    while eq and eq[0][0] <= t:
        # eq.get()
        heapq.heappop(eq)
        room -= 1
    room += 1
    roomMax = max(roomMax, room)

print(roomMax)