a = input()
a = a.split()
a = [int(i) for i in a]

baguni = [i for i in range(1,a[0]+1)]

for i in range(a[1]):
    b = input()
    b = b.split()
    b = [int(j) for j in b]
    temp = baguni[b[0]-1]
    baguni[b[0]-1] = baguni[b[1]-1]
    baguni[b[1]-1] = temp

for i in range(len(baguni)):
    print(baguni[i], end=' ')


