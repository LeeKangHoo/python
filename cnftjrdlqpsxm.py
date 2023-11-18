stamp2 = int(input())
price2 = int(input())

discount = [0]
temp = []
if 5 <= stamp2 :
    discount.append(500)
if 10 <=stamp2 :
    discount.append(price2*0.1)
if 15 <=stamp2 :
    discount.append(2000)
if 20 <= stamp2:
    discount.append(price2*0.25)

for i in range(len(discount)):
    temp.append(price2 - discount[i])

temp2 = min(temp)

if temp2 < 0:
    temp2 = 0

print(int(temp2))





