a = []
maximum = 0
count = 0

for i in range(9):
    a.append(int(input()))

maximum = max(a)

for i in range(9):
    if maximum == a[i]:
        count = i+1

print(maximum)
print(count)


