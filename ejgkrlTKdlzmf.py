num = int(input())
number = num
count = 0

while True:
        a = number //10
        b = number %10
        c = (a+b) % 10
        number = (b* 10) + c

        count += 1
        if(number == num):
            break

print(count)
