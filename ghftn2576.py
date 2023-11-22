a = []

for i in range(7):
    temp = int(input())
    if temp % 2 == 1:
        a.append(temp)
if a == []:
    print(-1)
else:
    print(sum(a))
    print(min(a))
    

