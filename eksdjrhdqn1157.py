a = input()

big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
big2 = []
small2 = []
cntarr = [0] * 26

count = 0


for i in big:
    big2.append(i)
for i in small:
    small2.append(i)

for i in a:
    for j in range(26):
        if big2[j] == i or small2[j] == i:
            cntarr[j] += 1

temp = 0

so = False
so2 = False
for i in range(26):
    if max(cntarr) == cntarr[i]:
        if so == False:
            so = True
            temp = i
        elif so == True:
            so2 = True
if so2 == True:
    print("?")
elif so2 == False:
    print(big[temp])



