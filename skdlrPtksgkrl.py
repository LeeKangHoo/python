a = input()
b = a.split()
b = [int(i) for i in b]
c = input()
d = c.split()
d = [int(i) for i in d]

if b[1] > d[1]:
    man = d[0]- b[0] - 1
elif b[1] == d[1]:
    if b[2] > d[2]:
        man = d[0] - b[0] - 1
    else:
        man = d[0]- b[0]
elif b[1] < d[1]:
    man = d[0] - b[0] 

se = d[0] - b[0] + 1
yeon = d[0] - b[0]


print(man)
print(se)
print(yeon)


