num = []
for i in range(5):
    num.append(int(input()))

print(int(sum(num)/len(num)))
num = sorted(num)
print(num[2])

