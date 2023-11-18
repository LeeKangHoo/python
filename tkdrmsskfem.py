burger = []
drink = []

for i in range(3):
    price = int(input())
    burger.append(price)
for i in range(2):
    price = int(input())
    drink.append(price)


sum = min(burger) + min(drink) - 50
print(sum)


