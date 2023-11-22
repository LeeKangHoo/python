a = [0, 0, 0]
for i in range(3):
    a[i] = input()
    
    
def count(temp):
    temp = [int(z) for z in temp]
    count = 0
    for i in range(len(temp)):
        if temp[i] == 0:
            count += 1 
    return int(count)


def dbc(temp):
    if temp == 0:
        print('E')
    elif temp == 1:
        print('A')
    elif temp == 2:
        print('B')
    elif temp == 3:
        print('C')
    elif temp == 4:
        print('D')


for i in range(3):
    dbc(count(a[i].split()))




