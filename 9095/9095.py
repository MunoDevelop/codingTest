# sys.stdin = open("input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # if test_case >1:
    #    break
    n = int(input())


    def find(n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            return find(n - 1) + find(n - 2) + find(n - 3)


    print(find(n))

    # ///////////////////////////////////////////////////////////////////////////////////
