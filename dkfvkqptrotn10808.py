a = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
final = [0] * 26

for i in a:
    cnt = 0
    for j in alpha:
        if j == i:
            final[cnt] += 1
        cnt += 1
            
for i in range(26):
    print(final[i],end=' ')

print('')



