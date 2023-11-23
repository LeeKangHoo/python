a = int(input())
final = []
count = 0
temp = 0
for i in range(a):
    b = input()
    for j in b:
        if j == 'O':
            count += 1
            temp += count
        elif j == 'X' :
            count = 0
    final.append(temp)
    temp = 0
    count = 0

for i in range(len(final)):
    print(final[i])
            


