import sys

n = int(sys.stdin.readline().rstrip())

lineone = [int(x) for x in sys.stdin.readline().rstrip().split()]

minWindow = [[0] * 3 for _ in range(2)]
maxWindow = [[0] * 3 for _ in range(2)]
for i in range(3):
    minWindow[0][i] = lineone[i]
    maxWindow[0][i] = lineone[i]
if n == 1:
    print(f'{max(maxWindow[0])} {min(minWindow[0])}')
else:
    for i in range(n-1):
        presentLine = [int(x) for x in sys.stdin.readline().rstrip().split()]

        minWindow[1][0] = min(minWindow[0][0], minWindow[0][1]) + presentLine[0]
        minWindow[1][1] = min(minWindow[0][0], minWindow[0][1], minWindow[0][2]) + presentLine[1]
        minWindow[1][2] = min(minWindow[0][1], minWindow[0][2]) + presentLine[2]

        maxWindow[1][0] = max(maxWindow[0][0], maxWindow[0][1]) + presentLine[0]
        maxWindow[1][1] = max(maxWindow[0][0], maxWindow[0][1], maxWindow[0][2]) + presentLine[1]
        maxWindow[1][2] = max(maxWindow[0][1], maxWindow[0][2]) + presentLine[2]

        for i in range(3):
            minWindow[0][i] = minWindow[1][i]
            maxWindow[0][i] = maxWindow[1][i]


    print(f'{max(maxWindow[1])} {min(minWindow[1])}')