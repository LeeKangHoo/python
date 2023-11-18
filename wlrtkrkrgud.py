num = input()
number = num.split()
number = [int(x) for x in number]

tempX = abs(number[0] - number[2])
tempY = abs(number[1] - number[3])

temp = [number[0], number[1], tempX, tempY]

print(min(temp))
