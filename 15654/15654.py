def fib(n, r):
    for i in range(r):
        if r == 0:
            r[0] = 0
        elif r == 1:
            r[1] = 1
        else:
            r[i] = r[i - 1] + r[i - 2]
    return r[n] % 1234567


def solution(n):
    r = [0] * n
    answer = 0
    return fib(n, r)