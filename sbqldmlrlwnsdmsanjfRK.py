

a = input()
b = a.split()
b = [int(i) for i in b]

if 2 < b[1] <= b[0]:
    print("OLDBIE!")
elif b[1] <= 2:
    print("NEWBIE!")
else:
    print("TLE!")
