inputList = [int(x) for x in input().split(" ")]
A = inputList[0]
B = inputList[1]
C = inputList[2]

print( (A+B)%C )
print( ((A%C) + (B%C))%C )
print(  (A*B)%C )
print( ((A%C) * (B%C))%C )