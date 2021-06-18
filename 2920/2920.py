lt = [int(x) for x in input().split()]
if lt == sorted(lt):
    print("ascending")
elif sorted(lt) == list(reversed(lt)):
    print("descending")
else:
    print("mixed")
