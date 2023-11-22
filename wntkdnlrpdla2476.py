a = int(input())
p = [0] * a

eqcount = [0] * a
eqnum = [0] * a
a2 = []
maximum = [0] * a

for i in range(a):
    a2.append(input())

for i in range (a):
    temp = a2[i].split()
    temp = [int(g) for g in temp]
    if temp[0] == temp[1]:
        eqnum[i] = temp[0]
        eqcount[i] += 1
    if temp[1] == temp[2]:
        eqnum[i] = temp[1]
        eqcount[i] += 1
    if temp[2] == temp[0]:
        eqnum[i] = temp[2]
        eqcount[i] += 1
    if eqcount[i] == 0:
        eqnum[i] = 0
    maximum[i] = max(temp)
    #print(eqcount,eqnum,a2,maximum)

for i in range(a):
    if eqcount[i] == 3:
        p[i] = 10000 + eqnum[i]*1000
    elif eqcount[i] == 1:
        p[i] = 1000 + eqnum[i]*100
    elif eqcount[i] == 0:
        p[i] = maximum[i] * 100
        
print(max(p))


