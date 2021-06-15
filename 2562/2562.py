lt = []
for i in range(9):
    lt.append(int(input()))
mx = max(lt)
print(max(lt))
print(lt.index(mx)+1)