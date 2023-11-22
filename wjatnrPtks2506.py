a = int(input())
b = input()
number = b.split()
number = [int(i) for i in number]
extraCount = 0
count = 0

for i in range(a):
    if number[i] == 1:
        count = count + 1 + extraCount
        extraCount += 1
    else :
        extraCount = 0

print(count)
