store = input()
complete = []
for i in range(int(store)):
    temp = input()
    temp2 = temp.split()
    temp2 = [int(i) for i in temp2]
    if temp2[1] - temp2[0] < 0:
        complete.append(999999)
    else:
        complete.append(temp2[1])

if min(complete) == 999999:
    print("-1")
else:
    print(min(complete))




