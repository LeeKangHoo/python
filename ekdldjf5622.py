a = input()
num = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
count = 0
for i in a:
    for j in range(8):
        
        for z in num[j]:
            if z == i:
                count += j+3
print(count)
    




