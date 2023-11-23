a = input()
b = a.split()
b = [int(i) for i in b]

if b == [1,2,3,4,5,6,7,8]:
    print("ascending")
elif b == [8,7,6,5,4,3,2,1]:
    print("descending")
else:
    print("mixed")






