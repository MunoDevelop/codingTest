import sys
from collections import Counter

N = int(input())
dict = {}

for i in range(26):
    dict[chr(65+i)] = 0

def divStr(str):
    for i in range(len(str)):
        dict[str[i]] += 10**(len(str)-(i+1))

for i in range(N):
    st = input()
    divStr(st)
s = 0
ix = 9
for i in Counter(dict).most_common(9):
    s += ix*i[1]
    ix -= 1
print(s)

