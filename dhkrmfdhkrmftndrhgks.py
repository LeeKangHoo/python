a = input()
b = a.split()

b = [int(num) for num in b]

if b[0]+b[1]+b[2] >= 100:
    print("OK")
else:
    if min(b) == b[0]:
        print("Soongsil")
    elif min(b) == b[1]:
        print("Korea")
    elif min(b) == b[2]:
        print("Hanyang")




