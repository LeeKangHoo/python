import sys

for a in range(3):
    num = int(sys.stdin.readline())
    sum = 0
    for b in range(num):
        temp = int(sys.stdin.readline())
        sum += temp

    if (sum<0):
        print("-")
    elif (sum > 0):
        print("+")
    else:
        print("0")


