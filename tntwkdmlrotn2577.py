a =[]
for i in range(3):
    a.append(int(input()))


num = a[0] * a[1] * a[2]
number = [0]*10
for i in str(num):
    number[int(i)] += 1

for i in range(10):
    print(number[i])

