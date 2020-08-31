import itertools
import copy

S = int(list(input().split())[1])

sequence = [int(x) for x in list(input().split())]
count = 0

for i in range(1,len(sequence)+1):
    for j in list(itertools.combinations(sequence,i)):
        if sum(j)==S:
            count+=1

print(count)