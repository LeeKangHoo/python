num = input()
number = num.split()


static = [1,1,2,2,2,8]
temp = []
for i in range(len(number)):
    number[i] = number[i] * (-1)

temp = static + number
print(temp)


