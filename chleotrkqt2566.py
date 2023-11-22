a = []
maximum = []
maximum2 = 0
count = 0
count2 = 0
for i in range(9):
    temp = input()
    b = temp.split()
    b = [int(i) for i in b]
    a.append(b)

for i in range(9):
    maximum.append(max(a[i]))
    maximum2 = max(maximum)
for i in range(9):
    if maximum[i] == maximum2:
        count2 = i+1

for i in range(9):
    if a[count2-1][i] == maximum2:
        count =  i+1
    

print(max(maximum))
print(count2,count)
