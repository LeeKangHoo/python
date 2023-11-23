a = input()
final = [-1] * 26
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(a)):
    abccount = 0
    for j in abc:
        acount = 0
        for z in a:
            if z == j and  final[abccount] == -1 :
                final[abccount] = acount 
            acount += 1
        abccount += 1

for i in range(len(abc)):
    print(final[i], end=' ')
print('')

