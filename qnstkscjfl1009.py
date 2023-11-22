f = int(input())

final = [0] * f

for i in range(f):
    num = input()
    temp = num.split()
    temp = [int(h) for h in temp]
    
    a = temp[0]
    b = temp[1]
    final[i] = a** b
    '''
    a = 0
    b = 0
    a = a % 10
    b = b % 10
    a = temp[0]
    b = temp[1]
    a = a ** b
    final[i] = a % 10
'''
for i in range(f):
    print(final[i])




