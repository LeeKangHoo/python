num = int(input())
num2 = []
for i in range(num):
    num2 += input()

D = 0
P = 0
for i in range(num):
    if D - 2 == P or P-2 == D:
        break
    else:
        if num2[i] == 'D':
            D += 1
        elif num2[i] == 'P':
            P += 1
    


print(str(D)+":"+str(P))

