def ccw(x1,y1,x2,y2,x3,y3):
    val = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    if val > 0:
        # 반시계
        return 1
    elif val == 0:
        # 일직선
        return 0
    elif val < 0:
        # 시계 방향
        return -1




x1,y1,x2,y2,x3,y3,x4,y4 = [int(x) for x in input().split()]


if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<0:
    print(1)
else:
    print(0)