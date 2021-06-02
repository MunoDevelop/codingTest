inputDum = input()
inputList = [int(x) for x in input().split(" ")]


def sol():
    return max(inputList) * min(inputList)


print(sol())