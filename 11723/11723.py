import sys

my_set = set()
for _ in range(int(input())):
    order = sys.stdin.readline().rsplit()

    if order[0] == 'add':
        my_set.add(int(order[1]))
    elif order[0] == 'remove':
        if int(order[1]) in my_set:
            my_set.remove(int(order[1]))
    elif order[0] == 'check':
        if int(order[1]) in my_set:
            print(1)
        else:
            print(0)
    elif order[0] == 'toggle':
        if int(order[1]) in my_set:
            my_set.remove(int(order[1]))
        else:
            my_set.add(int(order[1]))
    elif order[0] == 'all':
        my_set = set(range(1, 21))
    elif order[0] == 'empty':
        my_set.clear()