a = int(input())
final = []

for i in range(a):
    b = input()
    temp = b.split()
    temp2 = ''
    r = int(temp[0])
    s = temp[1]
    for j in s:
        for z in range(r):
            temp2 += j
    final.append(temp2)

for i in range(a):
    print(final[i])




