import sys

N, WMax = [int(x) for x in sys.stdin.readline().rstrip().split()]

# W,w,p 필요,초기i 는 len(w)-1
#0번째는 더미 데이터로
w = [0]
p = [0]
dp = {}
for i in range(N):
    a, b = [int(x) for x in sys.stdin.readline().rstrip().split()]
    w.append(a)
    p.append(b)


def pack(i, W):
    if i <= 0 or W <= 0:
        return 0
    # i 번째가 허용하는 max W 보다 더 무겁다.
    if w[i] > W:
        if (i-1, W) in dp:
            return dp[(i-1, W)]
        else:
            val = pack(i - 1, W)
            dp[(i-1, W)] = val
        return val
    else:
        # i 이전 item 까지 W 를 한계로 맞춤 (i번째 선택 안함)
        if (i-1,W) in dp:
            left = dp[(i-1,W)]
        else:
            left = pack(i - 1, W)
            dp[(i-1,W)] = left
        #i 번째 item을 선택해야 하기에 i 이전 item 까지 W-w[i](i 번째 item 을 선택한후 i이전 item을 w[i]무게만큼 빼고 계산
        if (i-1,W-w[i]) in dp:
            right = dp[(i-1,W-w[i])]
        else:
            right = pack(i - 1, W - w[i])
            dp[(i-1,W-w[i])] = right
        return max(left, p[i] + right)

print(pack(len(w) - 1, WMax))
