s = True
final = []

while s == True:
    a = int(input())
    if a == 0:
        s =False
    else:
        a2 = str(a)
        if a2 == a2[::-1]:
            final.append("yes")
        else : 
            final.append("no")
    if s == False:
        for i in final:
            print(i)
        break
